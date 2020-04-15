#!/bin/bash

## Convert justified text file (from pdf digitization) to csv

# Remove all headers except on the first page
grep -v $'^\f' $1 > $2;

# Replace multiple spaces with double spaces
counter=`grep -c '   ' $2`;
#echo ${counter}
while [ ${counter} -ne 0 ]; do
#    echo ${counter}
    sed -i 's/   /  /g' $2
    counter=`grep -c '   ' $2`;
done

# Remove all leading spaces
sed -i 's/^[ ]*//' $2

# Replace double spaces with quoted commas
sed -i 's/  /","/g' $2

#Add leading quote mark
sed -i 's/^/"/' $2

#Add trailing quote mark
sed -i 's/$/"/' $2

## Convert unicode to ascii
uni2ascii -B $2 > tmp
mv tmp $2


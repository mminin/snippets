# Reorders CSV and adds an extra column (with the callback value of certificate)
# Usage: python3 reorderCSV.py inputCSV inputHeader certNum outputCSV

# Example use:

# for i in joinedG1/*; do
#     certNum=`echo $(basename $i) | sed 's/_1_joined.csv//g'`;
#     python3 reorderCSV.py $i commonHeader.csv $certNum reorderedG1/$certNum.csv;
# done

import sys
import csv
inputCSV=sys.argv[1]
inputHeader=sys.argv[2]
certNum=sys.argv[3]
outputCSV=sys.argv[4]
with open(inputHeader) as f: header=list(csv.reader(f))[0]+['CertNum']
with open(inputCSV) as f: data=list(csv.DictReader(f))
with open(outputCSV,'w') as f:
    w=csv.DictWriter(f,fieldnames=header)
    w.writeheader()
    for row in data:
        d=dict(row)
        d['CertNum']=certNum
        w.writerow(d)

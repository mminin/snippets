#this will add a new column to the csv, computed from some other columns
#edit the first half to replace column name and the function to generate values provided row

from astropy.time import Time
columnName="YourColumnName" # replace this with name of your column
def myValFunct(row): # replace this with ad-hoc function
    t=row[3]
    myDate=t.split(' ')[0]
    myTime=t.split(' ')[1]
    myVal=Time(myDate.replace(':','-')+'T'+myTime,scale='utc').jd
    return myVal

#### Don't touch the code below, it's doing I/O stuff
import csv
import sys
finN=sys.argv[1]
foutN=sys.argv[2]
with open(finN) as fin:q=list(csv.reader(fin))
q[0].append(columnName)
for row in q[1:]:row.append(str(myValFunct(row)))
with open(foutN,'w') as fout: csv.writer(fout).writerows(q)

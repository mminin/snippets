columnName="CameraYaw" # replace this with name of your column
#### Don't touch the code below, it's doing I/O stuff
import csv
import sys
finN=sys.argv[1]
finA=sys.argv[2]
with open(finA) as fin:qa=dict(csv.reader(fin))
foutN=sys.argv[3]
with open(finN) as fin:q=list(csv.reader(fin))
q[0].append(columnName)

#EDIT THIS PART
def myValFunct(row): # replace this with ad-hoc function
    t=row[0]
    myVal=qa[t]
    return myVal

for row in q[1:]:row.append(str(myValFunct(row)))
with open(foutN,'w') as fout: csv.writer(fout).writerows(q)

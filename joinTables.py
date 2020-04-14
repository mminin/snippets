## This script joins three csv files based on a common field

import csv
import sys

InFile1=sys.argv[1]
keyCol1=sys.argv[2]
InFile2=sys.argv[3]
keyCol2=sys.argv[4]
InFile3=sys.argv[5]
keyCol3=sys.argv[6]

f1=[]
f2=[]
f3=[]
with open(InFile1) as _: f1=list(csv.DictReader(_))
with open(InFile2) as _: f2=list(csv.DictReader(_))
with open(InFile3) as _: f3=list(csv.DictReader(_))
fields=list(f1[0].keys()) + [
    _ for _ in f2[0].keys() if _ != keyCol2] + [
    _ for _ in f3[0].keys() if _ != keyCol3]

allKeys={_[keyCol1] for _ in f1}.union(
    {_[keyCol2] for _ in f2}).union({_[keyCol3] for _ in f3})

def joinRow(k):
    tmp=[_ for _ in f1 if _[keyCol1]==k][0]
    tmp.update([_ for _ in f2 if _[keyCol2]==k][0])
    tmp.update([_ for _ in f3 if _[keyCol3]==k][0])
    return tmp

with open("output.csv","w") as f:
    w=csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for k in allKeys:
        w.writerow(joinRow(k))

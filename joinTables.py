## This script joins three csv files based on a common field

import csv
import sys
import functools

InFiles=[_ for _ in sys.argv[1::2]]
InKeys=[_ for _ in sys.argv[2::2]]

fs=[]

for InFile in InFiles:
    with open(InFile) as _: fs.append(list(csv.DictReader(_)))

filesAndKeys=list(zip(fs, InKeys))

fields=list(fs[0][0].keys())
print(fields)

getNewKeys=lambda f,k: [_ for _ in f[0].keys() if _ != k]

fields += functools.reduce(lambda a,b:a+b,[getNewKeys(*_) for _ in filesAndKeys[1:]])

print(fields)

allKeys=set.union(*[{_[k] for _ in f} for f,k in filesAndKeys])
print(allKeys)

print(filesAndKeys[0][1])


def joinRow(k):
#    print(k)
    #tmp=[_ for _ in filesAndKeys[0][0] if _[filesAndKeys[0][1]]==k][0]
    tmp=dict()
#    print(tmp)
#    for f, InKey in filesAndKeys[1:]:
    for f, InKey in filesAndKeys:
        if k in allKeys:
            klist=[_ for _ in f if _[InKey]==k]
            if len(klist)>0:
#                print('DEBUG %s'%(klist[0]))
#                print('updating..')
                tmp.update(klist[0])
#                print('updated')
    return tmp

with open("output.csv","w") as f:
    w=csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for k in allKeys:
#        print(k)
        row=joinRow(k)
#        print(row)
        w.writerow(row)

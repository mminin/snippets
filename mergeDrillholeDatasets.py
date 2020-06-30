# This script will merge well logs datasets by splitting logs into unique segments 
# based on overlapping depth intervals:

import collections

import csv
import os

filenames=os.listdir('input')

def getFData(filenames):
    fdata=[]
    for fname in filenames:
        with open('input/%s'%fname) as f:
            #print(fname)
            r=csv.DictReader(f)
            q=[_ for _ in r]
            fdata.append(q)
    return fdata

fdata=getFData(filenames)

# Get all fieldnames:
def getFieldnames(fdata):
    d = collections.OrderedDict([])
    for q in [_[0] for _ in fdata]:
        d.update(q)
    fieldnames=list(d.keys())
    return fieldnames

fieldnames=getFieldnames(fdata)

# Get all unique holes
allHoles=list({_ for _ in [[_['HOLE_ID'] for _ in q] for q in fdata] for _ in _})
allHoles.sort()

#for every hole we must see which unique depths exist:

getAllFromDepths=lambda HoleID: {w['From_m'] for s in fdata for w in s if w['HOLE_ID']==HoleID}
getAllToDepths=lambda HoleID: {w['To_m'] for s in fdata for w in s if w['HOLE_ID']==HoleID}

getAllDepths=lambda HoleID:set.union(getAllFromDepths(HoleID),getAllToDepths(HoleID))

getAllDepthsSorted=lambda _: sorted(list(getAllDepths(_)),key=lambda _: float(_))

getAllDataForHoleID=lambda HoleID: [[_ for _ in q  if _['HOLE_ID']==HoleID] for q in fdata]

## Then for each interval there should be only one 
## unique match in each of the tables
## Where From_m <= local_from and To_m >= local_to
## For each of the holes.
## We should do this one hole at a time...
def getGranule(HoleData, start, end):
    extract=[[_ for _ in z if float(_['From_m'])<=float(start) and float(_['To_m'])>=float(end)] for z in HoleData]
    d1 = collections.OrderedDict([])
    for i in [_ for _ in extract if _!=[]]:
        d1.update(i[0])
    d2 = collections.OrderedDict([('From_m', start), ('To_m', end)])
    d1.update(d2)
    return d1



def getAllGranulesForHoleID(HoleID):
    result=[]
    HoleData=getAllDataForHoleID(HoleID)
    HoleData=[_ for _ in HoleData if _!=[]]
    HoleDepths=getAllDepthsSorted(HoleID)
    for local_from,local_to in list(zip(HoleDepths[:-1],HoleDepths[1:])):
        result.append(getGranule(HoleData,local_from,local_to))
    return result

def getAllGranules(allHoles):
    result=[]
    for HoleID in allHoles:
        result.extend(getAllGranulesForHoleID(HoleID))
    return result

allGranules=getAllGranules(allHoles)

with open('output.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=fieldnames)
    w.writeheader()
    for granule in allGranules:
        w.writerow(granule)





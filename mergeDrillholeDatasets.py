# This script will merge well logs datasets by splitting logs into unique segments 
# based on overlapping depth intervals, it assumes there key columns are named as
# HOLE_ID, From_m, To_m (This can be edited in the script settings)
# The source data should be in directory called "input"
# the output would be saved as output.csv

import collections

import csv
import os

# SETTINGS
colname_HoleID='HOLE_ID'
colname_From='From_m'
colname_To='From_to'

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
allHoles=list({_ for _ in [[_[colname_HoleID] for _ in q] for q in fdata] for _ in _})
allHoles.sort()

#for every hole we must see which unique depths exist:

getAllFromDepths=lambda HoleID: {w[colname_From] for s in fdata for w in s if w[colname_HoleID]==HoleID}
getAllToDepths=lambda HoleID: {w[colname_To] for s in fdata for w in s if w[colname_HoleID]==HoleID}

getAllDepths=lambda HoleID:set.union(getAllFromDepths(HoleID),getAllToDepths(HoleID))

getAllDepthsSorted=lambda _: sorted(list(getAllDepths(_)),key=lambda _: float(_))

getAllDataForHoleID=lambda HoleID: [[_ for _ in q  if _[colname_HoleID]==HoleID] for q in fdata]

## Then for each interval there should be only one 
## unique match in each of the tables
## Where From_m <= local_from and To_m >= local_to
## For each of the holes.
## We should do this one hole at a time...
def getGranule(HoleData, start, end):
    extract=[[_ for _ in z if float(_[colname_From])<=float(start) and float(_[colname_To])>=float(end)] for z in HoleData]
    d1 = collections.OrderedDict([])
    for i in [_ for _ in extract if _!=[]]:
        d1.update(i[0])
    d2 = collections.OrderedDict([(colname_From, start), (colname_To, end)])
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





### This code finds CTX stereopairs via requests to ODE REST
### given bounding box and min/max of delta emission angle.
## To use say: python ctxStereo02.py westlon eastlon minlat maxlat minDeltaEm maxDeltaEm
## EXAMPLE: python ctxStereo02.py 12 13 12 13 1 5

import sys
import json
import urllib
from xml.dom.minidom import parseString
import requests
#from pprint import pprint
import shapely.wkt

if len(sys.argv)!=7: print("Incorrect number of arguments!\nUsage:\
    python ctxStereo02.py westlon eastlon minlat maxlat minDeltaEm maxDeltaEm"); quit()
westlon,eastlon,minlat,maxlat,minDeltaEm,maxDeltaEm=sys.argv[1:]
minDeltaEm,maxDeltaEm=float(minDeltaEm),float(maxDeltaEm)
baseURL="http://oderest.rsl.wustl.edu/live2/?"+\
        "target=mars&query=product&results=cm&output=XML&pt=EDR&iid=CTX&ihid=MRO&"
odeURL=baseURL+"&westlon="+westlon+"&eastlon="+eastlon+"&minlat="+minlat+"&maxlat="+maxlat
print(odeURL)
myDoc=parseString(requests.get(odeURL).text)
q=int(myDoc.getElementsByTagName("Count")[0].childNodes[0].data)
if q == 100:
    print("Bounding box too large! Maximum number of coverages reached."); quit()
if q == 0:
    print("No coverages found!"); quit()
print("Total number of coverages is "+str(q))
prodList=[]
for product in myDoc.getElementsByTagName("Product"):
    q=lambda tag: product.getElementsByTagName(tag)[0].childNodes[0].data
    prodList.append([q("Footprint_geometry"),
                     q("LabelURL").split('/')[-1].split('.')[0],
                     float(q("Emission_angle"))])
prodList.sort(key=lambda q:q[2])
matches=[]
for i in range(len(prodList)):
    subList=prodList[i:]
    for j in range(len(subList)):
        deltaEm=abs(prodList[i][2]-subList[j][2])
        if (deltaEm<maxDeltaEm) & (deltaEm>minDeltaEm):
            matches.append([prodList[i],subList[j],deltaEm])

stereopairs=[]
for match in matches:
    mA=shapely.wkt.loads(match[0][0])
    mB=shapely.wkt.loads(match[1][0])
    smallerArea=[mA.area,mB.area][mA.area>mB.area]
    intersectionArea=mA.intersection(mB).area
    if intersectionArea>0:
        stereopairs.append([match[0],match[1],match[2],intersectionArea/smallerArea])

if len(stereopairs)==0: print("No matches found!");quit()

stereopairs.sort(key=lambda q:q[3])

print("Total of " + str(len(stereopairs)) + " stereopairs found.")
for sp in stereopairs:
    print( "\nPair " + sp[0][1] + " and " + sp[1][1])
    print( "DeltaEm = " + str(sp[2]) + " degrees")
    print( "Overlap = " + str(int(sp[3]*100)) + " percent" )

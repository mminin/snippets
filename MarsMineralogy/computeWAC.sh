#!/usr/bin/davinci -f
#
# Computes with Davinci the Weighted Absorption Centre (WAC) 
# from unrectified THEMIS Emission bands 3,4,5,6,7,8,9 QUB
# returned by THMPROC.
#
# The output file will lose projection and geotransform,
# but this can be copied over from the original file  (Emissions QUB) 
# using gdalcopyproj.py
#
cube=read($1)
inversed=1-cube
wl={7.93, 8.56, 9.35, 10.21, 11.04, 11.79, 12.67}
wla=create(z=length(wl), format=float)
for(i=1;i<=length(wl);i+=1){
 wla[0:0,0:0,i]=wl[i]
}
dwla=wla[0:0,0:0,2:length(wla)]-wla[0:0,0:0,1:length(wla)-1]
triangles=abs(inversed[0:0,0:0,1:6]-inversed[0:0,0:0,2:7])/2
squares=min(inversed[0:0,0:0,1:2],axis=z)
for(i=2;i<7;i+=1){
 squares=cat(squares,min(inversed[0:0,0:0,i:i+1],axis=z),axis=z)
}
trapesoids=(squares+triangles)*dwla
cumsum=sum(trapesoids[0:0,0:0,1:1],axis=z)*0
for(i=1;i<=6;i+=1){
 cumsum=cat(cumsum,sum(trapesoids[0:0,0:0,0:i],axis=z),axis=z)
}
midval=cumsum[0:0,0:0,7]/2
idxMin=int(sum(cumsum<midval,axis=z))
cumsumIdxMin=idxMin*0
cumsumIdxMax=idxMin*0
for(i=1;i<=6;i+=1){
 cumsumIdxMin+=(idxMin==i)*cumsum[0:0,0:0,i]
 cumsumIdxMax+=(idxMin==i)*cumsum[0:0,0:0,i+1]
}
midvalxd=(midval-cumsumIdxMin)/(cumsumIdxMax-cumsumIdxMin)
wacWlIdxMin=idxMin*0
wacWlIdxMax=idxMin*0
for(i=1;i<=6;i+=1){
 wacWlIdxMin+=(idxMin==i)*wla[0:0,0:0,i]
 wacWlIdxMax+=(idxMin==i)*wla[0:0,0:0,i+1]
}
xLoc=midvalxd*(wacWlIdxMax-wacWlIdxMin)+wacWlIdxMin
xLocDat=xLoc*(cube[0:0,0:0,1]!=-32768)
write(object=xLocDat, filename=$2, type=tiff, force=1)




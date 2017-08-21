#script rolls image halfway around.
#very usefull for rolling maps over from -180 -> 180 to 0 -> 360
#usage: python imageRoll.py input.jpg output.jpg
from scipy import misc
import numpy as np
import sys
name=sys.argv[1]
outputName=sys.argv[2]
data=misc.imread(name)
width=data.shape[1]
output=np.roll(data,int(width/2),1)
misc.imsave(outputName,output)

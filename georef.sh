#!/bin/sh

#Usage: georef.sh input.jpg output.tif
#Files must have EXIF_GPS tags
#Three lines below control projection and image size (in degrees)
#The image is only georeferenced. No reprojection/wrapping, scale is arbitrary

LAToffset='1.000'
LONoffset='1.633'
projection='EPSG:4269'

LAT=$(gdalinfo $1 | grep EXIF_GPSLatitude | sed s/EXIF_GPSLatitude=// | sed 's/[\(\)]//g')

LATdeg=$(echo $LAT | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\1 /')
LATmin=$(echo $LAT | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\2 /')
LATsec=$(echo $LAT | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\3 /')

LON=$(gdalinfo $1 | grep EXIF_GPSLongitude | sed s/EXIF_GPSLongitude=// | sed 's/[\(\)]//g')

LONdeg=$(echo $LON | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\1 /')
LONmin=$(echo $LON | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\2 /')
LONsec=$(echo $LON | sed 's/\([^ ]*\) \([^ ]*\) \([^ ]*\)/\3 /')

LONfloat=$(echo $LONdeg+$LONmin/60+$LONsec/\(60*60\)| bc -l)
LATfloat=$(echo $LATdeg+$LATmin/60+$LATsec/\(60*60\)| bc -l)

LATflAdd=$(echo $LATfloat+$LAToffset | bc -l)
LONflAdd=$(echo $LONfloat+$LONoffset | bc -l)

echo $LONfloat $LONflAdd
echo $LATfloat $LATflAdd

#gdal_translate -of GTiff -a_ullr ullon ullat lrlon lrlat -a_srs EPSG:4269 input.tif output.tif
gdal_translate -of GTiff -a_ullr $LONfloat $LATflAdd $LONflAdd $LATfloat -a_srs $projection $1 $2

# bits and pieces

With bash make previews by resizing/resampling all big photos in a directory:

     for f in 0_ALL-PHOTOS/*.JPG; do s=${f##*/}; convert 0_ALL-PHOTOS/${s} -resize 200 0_ALL_PHOTOS_SMALL/${s%.*}_browse.png; done;

-------------
With python read a CSV file containing multi-character separator (e.g. ',\t'):
```
import csv
with open("SearchResults.csv") as _:
    _=csv.reader((_.replace(',\t',',') for _ in _), delimiter=',')
    CSV_header,CSV_data=next(_),[*_]
```
Same but return an ordered dict instead of list:

    with open("SearchResults.csv") as _: CSV_dict=[*csv.DictReader(_.replace(',\t',',') for _ in _)]

--------------
With python remove multiple characters from a string:
```
myString='        BAND_BIN_BAND_NUMBER = (4, 9, 10)'
toRemove='( )'
print(''.join([{_:'' for _ in toRemove}.get(_, _) for _ in myString]))
#Output: 'BAND_BIN_BAND_NUMBER=4,9,10'
```
--------------
Remove double spaces from file names in bash:
```
while read i; do mv "${i}" "$(echo ${i} | sed 's/  / /g')"; done << EOF
$(ls)
EOF
```
--------------
Docker build and run image:
```
docker build . -t <imageName>:<versionTag>;docker run -it $_
```
--------------
To check version of the python package:
```
python -c "import csv as _; print(_.__version__)"
```
--------------
Unzip all files into one directory and replace nested folders with underscore prefexes (flatten tree).
```
# first unzip into directories with the same name as archive, then remove zips
for i in $(ls *.zip);
 do mkdir ${i%.*};
 unzip $i -d ${i%.*};
 rm $i;
done;

# now walk the tree and move the files
for i in $(tree -Fif | grep -v /$ | grep /);
 do mv $i $(echo $i | tr '/' '_' | sed 's/^..//');
done

# remove all directories
rm -r $(ls -d */)
```
--------------
To use pprint instead of print everywhere in py3:
```
from pprint import pprint as print
```
--------------
Print keys in a json file from bash
```
python3 -c "import json; f=open('/path/to/file'); [print(_) for _ in json.load(f).keys()]; f.close()"
```
--------------
To embed images in html: 

1. Convert image to base64
```
base64 someImage.png > someImage.png.base64
```
2. Place code into the page like so:
```
<img src="data:image/jpg;base64,
{BASE 64 IMAGE DATA}
" style="width:100%" />
```
3. In case the image repeats multiple times on the page use JS:
```
var base64Data=[
"/9j/4AAQSkZJRgABAQEASwBLAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcG",
"a1Srt2/zPz3iTi1U74XAv3usu3kvPz6dNdn3V3LfXMk00jyzSsWd3OWY+pNR0UV7yR+ZNtu7Ciii",
"gQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH//Z"
].join("");

var img = "url('data:image/png;base64, "+base64Data + "')";
var x = document.getElementsByClassName("header");
var i;
for (i = 0; i < x.length; i++) {
//  x[i].style.backgroundImage = img;
} 
```
To make this directly usable in JS, use the following script
```
#!/bin/bash
echo "var base64Data=[" > $2
base64 $1 | while read -r; do printf '"%s",\n' "$REPLY"; done >> $2
echo "].join(\"\");" >> $2
```
--------------
Flatten nested  list:
```
[i for j in [[1,2],[3,4],[5,6]] for i in j]
```
--------------
Get links from file
```
cat index.html | grep -o -P '(?<=href\=\").*(?=\")'
```
--------------
Plot geochemistry in QGIS replacing less than values with 0's:
```
if( regexp_match( "Au_x_ppb", '\\s<' ) ,0, to_real("Au_x_ppb"))/if( regexp_match( "Ag_ppm", '\\s<' ) ,0, to_real("Ag_ppm"))
```
--------------
Create python anonymous class object:
```
f=type("", (), {})()
```
--------------
Rotate point around another point
```
def rotatePnt(org,pt,th):
    #ensure points are numpy arrays
    org=np.asarray(org)
    pt=np.asarray(pt)
    # translate point to the origin
    pt=pt-org
    #apply rotation
    rotationMtrx=np.asarray([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    pt=np.dot(rotationMtrx,pt)
    #restore point
    pt=pt+org
    return pt

## Example use
testLine=[[1,1],[4,3],[5,7],[8,1],[4,3]]
unwrapLine=lambda _: [[_[0] for _ in _],[_[1] for _ in _]]
plt.plot(*unwrapLine(testLine))
for i in range(10,360,10):
    plt.plot(*unwrapLine([rotatePnt([1,1],_,np.radians(i)) for _ in testLine]))
```
--------------
Clean read-only filesystem error on usb:
```
sudo dosfsck -r -v /dev/sde1
```
--------------
Convert xlsx to csv:
```
for i in $(seq 1 19); do xlsx2csv input.xlsx -s $i > csv/$i.csv;done
```
Convert xls to csv:
```
for i in $(seq 1 19); do xls2csv input.xls -s $i > csv/$i.csv;done

```
Convert ods to csv:
```
libreoffice --headless --convert-to csv --outdir csv *
```
--------------
Replace "< " with "-" in a csv:
```
for i in $(ls *.csv); do sed -i 's/< /-/g' $i;done
```
Replace "> some_value" with "-888" in csv (replace overlimit with "-888"):
```
sed -i 's/> [0-9\.][0-9\.]*/-888/g' AR-ICP.csv 
```
--------------
Calculate sample id's from grid X/Y coordinates in QGIS3:
```
if(length("X")<3,lpad("X",3,0),"X") +'E '+to_string(if(Y>=0,lpad(abs("Y"),3,0),abs("Y")))+if("Y"<0,'S','N')
```
--------------
List unique headers in a several numbered folders containing multiple csv tables:
```
head -qn 1 tableGroupNumber*/* | sort | uniq > uniqueHeaders.csv
```
Combine unique headers in bash with python while preserving the order (new keys are added to the end of the list):
```
python3 -c "import csv; from functools import reduce; f=open(\"uniqueHeaders.csv\"); rows=list(csv.reader(f)); result=reduce(lambda a,b: a+(list(set(b)-set(a))),rows); print(\",\".join(result))"
```
--------------
Check if a CSV file has duplicate values in the first column:
```
sort input.csv | cut -d "," -f1 | uniq -d
```
Cut out the first 3 columns from a CSV (assuming no data values has commas):
```
cut -d "," -f 1-3 input.csv > output.csv
```
--------------
Replace space with underscore between two numbers only if the second number is followed by a column (useful for cleaning date-time fields in CSV):
```
sed 's/\([0-9]\)[[:space:]]\([0-9]*[0-9]:\)/\1_\2/g'
```


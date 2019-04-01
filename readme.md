# bits and pieces

Here is a batch command to make previews by resizing/resampling all big photos in a directory:

     for f in 0_ALL-PHOTOS/*.JPG; do s=${f##*/}; convert 0_ALL-PHOTOS/${s} -resize 200 0_ALL_PHOTOS_SMALL/${s%.*}_browse.png; done;

-------------
Read with python a CSV file that uses multi-character separator (e.g. ',\t'):
```
import csv
with open("SearchResults.csv") as f:
    r=csv.reader((_.replace(',\t',',') for _ in f), delimiter=',')
    CSV_header,CSV_data=next(r),[*r]
```

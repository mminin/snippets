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
--------------

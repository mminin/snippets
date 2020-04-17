# Use python3
# This script will stack all csv tables in a folder into a single table.
# This will not preserve column order, sorry.
# The result will be output as output.csv
# Usage: 
# python3 stackCsvTables.py [sourceDirectory] [output file]
# Example: 
# python3 stackCsvTables.py INAA INNA.csv

import csv
import sys
import os

dataDir=sys.argv[1]
filepaths=['/'.join([dataDir,_]) for _ in os.listdir(dataDir)]
ds=[]
for filepath in filepaths:
    with open(filepath) as f:
        d=list(csv.DictReader(f))
        ds.append(d)

allKeys={_ for _ in [_[0].keys() for _ in ds] for _ in _}

with open(sys.argv[2], "w") as f:
    w=csv.DictWriter(f,fieldnames=allKeys)
    w.writeheader()
    for d in ds:
        w.writerows(d)

'''
This script will merge two CSV tables by depths.

Example: 
Left table:
  WellID, from_m, to_m, data1, data2
  W1, 10, 15, A, B

Right table:
  WellID, from_m, to_m, data3, data4
  W1, 12, 20, C, D

Output table:
  WellID, from_m, to_m, data1, data2, data3, data4
  W1, 10, 12, A, B, null, null
  W1, 12, 15, A, B, C, D
  W1, 15, 20, null, null, C, D

Script assues that the data is grouped (ie there are multiple wells with recorded data)

Example use:

python3 depthsMixer.py data/geochem.csv data/stratigraphy.csv results/mergedChemStrat.csv Well_ID from_ft to_ft

'''

import csv
import os
import pandas as pd
from pandas.io.parsers import StringIO
from pandasql import sqldf
import sys

fileName_TableLeft=sys.argv[1] # path to the LEFT table to join
fileName_TableRight=sys.argv[2] # path to the RIGHT table to join
resultTable=sys.argv[3] # path to the output table

joinOnFieldName=sys.argv[4] # key on which to group data, eg. "Well ID".
fromFieldName=sys.argv[5] # from distance field name, eg "from_m"
toFieldName=sys.argv[6] # from distance field name, eg "to_m"

data_TableLeft=pd.read_csv(fileName_TableLeft,encoding='latin1')
data_TableRight=pd.read_csv(fileName_TableRight,encoding='latin1')

def getMeterages(data_pd):
    from_meterage=pd.DataFrame(data_pd[[joinOnFieldName,fromFieldName]]).rename(columns={fromFieldName: 'Meterage'}, inplace=False)
    to_meterage=pd.DataFrame(data_pd[[joinOnFieldName,toFieldName]]).rename(columns={toFieldName: 'Meterage'}, inplace=False)
    return pd.concat([from_meterage,to_meterage]).drop_duplicates()

borders=pd.concat([getMeterages(data_TableLeft),getMeterages(data_TableRight)]).drop_duplicates()

bounds=pd.merge(borders.rename(columns={'Meterage': 'from_ival'}), 
                borders.rename(columns={'Meterage': 'to_ival'}), 
                on=joinOnFieldName).query('to_ival>from_ival')

calcIvals=bounds.groupby([joinOnFieldName,'from_ival']).agg({'to_ival':'min'}).reset_index()

def dbGetQuery(q):
    return sqldf(q, globals())

query_TableLeft_new= """
SELECT data_TableLeft.* FROM calcIvals LEFT JOIN data_TableLeft ON 
calcIvals.%s  = data_TableLeft.%s AND (%s >=to_ival) 
AND (%s <=from_ival);
"""%(joinOnFieldName,joinOnFieldName,toFieldName,fromFieldName)

data_TableLeft_new = dbGetQuery(query_TableLeft_new)

query_TableRight_new= """
SELECT data_TableRight.* FROM calcIvals JOIN data_TableRight ON 
calcIvals.%s  = data_TableRight.%s AND (%s >=to_ival) 
AND (%s <=from_ival);
"""%(joinOnFieldName,joinOnFieldName,toFieldName,fromFieldName)

data_TableRight_new = dbGetQuery(query_TableRight_new)


calcIvals=calcIvals.rename(columns={'from_ival': fromFieldName}).rename(columns={'to_ival': toFieldName})

def drop_joined(df):
    # list comprehension of the cols that end with '_joined'
    to_drop = [x for x in df if x.endswith('_joined')]
    df.drop(to_drop, axis=1, inplace=True)

data_merged_left=pd.merge(calcIvals, data_TableLeft_new, 
         on=[joinOnFieldName,fromFieldName,toFieldName], how='left', suffixes=('', '_joined'))

drop_joined(data_merged_left)

data_merged_results=pd.merge(data_merged_left, data_TableRight_new, 
         on=[joinOnFieldName,fromFieldName,toFieldName], how='left', suffixes=('', '_joined'))

## Write output
data_merged_results.to_csv(resultTable)


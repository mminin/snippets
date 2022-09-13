# Usage merge_depths_pandas.py left_csv_path right_csv_path right_suffix result_csv_path
# Script uses pandas to outer-join two tables by depth intervals

import pandas as pd
import numpy as np
import chardet
import sys
from more_itertools import sliced

################

CHUNK_SIZE=100000
TMP_FILE='TMP_CHUNKS.csv'

master_table_path=sys.argv[1]
slave_table_path=sys.argv[2]
right_suffix=sys.argv[3]
result_table_path=sys.argv[4]

FIELD_HOLE_ID='hole_id'






def get_encoding(filepath):
    with open(filepath, 'rb') as f:
        encoding = chardet.detect(f.read())['encoding']
    return encoding

def getDepths(df):
    return pd.concat([df[[FIELD_HOLE_ID,'from_m']].rename(columns={'from_m':'depth_m'}),
               df[[FIELD_HOLE_ID,'to_m']].rename(columns={'to_m':'depth_m'})]).drop_duplicates()

def getAllDepts(ldf):
    return pd.concat([getDepths(_) for _ in ldf]).drop_duplicates().sort_values('depth_m')

#def filter_bigdata_by_chunks(df, bool_series):
#    df['my_filter']=bool_series
#    df.round({'from_m':2,'to_m':2}).to_csv(TMP_FILE, index=False)
#    results=[]
##    for index_slice in sliced(range(len(df)), CHUNK_SIZE):
##        g = df.iloc[index_slice]
#    for chunk in pd.read_csv(TMP_FILE, chunksize=CHUNK_SIZE, low_memory=False):
#        results.append(chunk[chunk['my_filter']].drop(columns=['my_filter', 'from_m%s'%right_suffix,'to_m%s'%right_suffix]))
#    return pd.concat(results)

def merge_table(master, slave):
    master['my_master_index']=master.index
    slave['my_slave_index']=slave.index
    master_subset=master[[FIELD_HOLE_ID, 'from_m', 'to_m','my_master_index']].copy()
    slave_subset=slave[[FIELD_HOLE_ID, 'from_m', 'to_m','my_slave_index']].copy()
    merged_df=pd.merge(master_subset, slave_subset, how='inner', on=[FIELD_HOLE_ID],
                       suffixes=('', right_suffix), copy=False)
    bool_series = (merged_df['from_m']>=merged_df['from_m%s'%right_suffix]) & (merged_df['to_m']<=merged_df['to_m%s'%right_suffix])
    #merged_df.query("@bool_series", inplace=True)
    #merged_df=filter_bigdata_by_chunks(merged_df, bool_series)
    #bool_series = 
    #merged_df.query("@bool_series", inplace=True)
    #merged_df.drop(columns=['from_m%s'%right_suffix,'to_m%s'%right_suffix], inplace=True)
    #merged_df=filter_bigdata_by_chunks(merged_df, bool_series)
    merged_df=merged_df[bool_series]
    merged_df=pd.merge(merged_df, master, how='inner', on=['my_master_index'], suffixes=('', right_suffix), copy=False)
    merged_df.drop(columns=['%s%s'%(FIELD_HOLE_ID,right_suffix), 'from_m%s'%right_suffix, 'to_m%s'%right_suffix], inplace=True)
    merged_df.drop(columns=['my_master_index'], inplace=True)
    merged_df=pd.merge(merged_df, slave, how='inner', on=['my_slave_index'], suffixes=('', right_suffix), copy=False)
    merged_df.drop(columns=['%s%s'%(FIELD_HOLE_ID,right_suffix), 'from_m%s'%right_suffix, 'to_m%s'%right_suffix], inplace=True)
    merged_df.drop(columns=['my_slave_index'], inplace=True)
    #print(merged_df.columns)
    return merged_df.drop_duplicates()

def remove_suffix_right(df):
    bad_columns=[_ for _ in df.columns if _.endswith('_right')]
    df.drop(columns=bad_columns, inplace=True)

df_master = pd.read_csv(master_table_path, encoding=get_encoding(master_table_path), low_memory=False, dtype={'From_m':np.float32,'To_m':np.float32}).rename(columns={'From_m':'from_m','To_m':'to_m'})
df_slave = pd.read_csv(slave_table_path, encoding=get_encoding(slave_table_path),low_memory=False, dtype={'From_m':np.float32,'To_m':np.float32}).rename(columns={'From_m':'from_m','To_m':'to_m'})

all_depths=getAllDepts([df_master,df_slave])
all_depths['to_m']=all_depths.groupby(FIELD_HOLE_ID).shift(-1)['depth_m']

all_depths.dropna(inplace=True)
all_depths.rename(columns={'depth_m':'from_m'},inplace=True)

df_merged_1 = merge_table(all_depths, df_master)
df_merged = merge_table(df_merged_1, df_slave)

df_void = pd.merge(df_merged_1, df_merged, how='outer', on=[FIELD_HOLE_ID, 'from_m', 'to_m'], 
           suffixes=('', '_right'), indicator=True)

remove_suffix_right(df_void)
df_void = df_void[df_void['_merge']=='left_only']
df_void.drop(columns=['_merge'], inplace=True)

df_merged.reset_index(inplace=True, drop=True)
df_void.reset_index(inplace=True, drop=True)


df_result = pd.concat([df_merged,df_void], ignore_index=True)

df_result.sort_values([FIELD_HOLE_ID, 'from_m'], inplace=True)

df_result=df_result.round({'from_m':2,'to_m':2})
df_result=df_result[df_result['from_m']!=df_result['to_m']]
if 'my_master_index' in df_result.columns:
    df_result.drop(columns=['my_master_index'], inplace=True)
df_result.to_csv(result_table_path, index=False)


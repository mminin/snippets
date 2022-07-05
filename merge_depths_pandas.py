# Usage merge_depths_pandas.py left_csv_path right_csv_path right_suffix result_csv_path
# Script uses pandas to outer-join two tables by depth intervals

import pandas as pd
import sys

master_table_path=sys.argv[1]
slave_table_path=sys.argv[2]
right_suffix=sys.argv[3]
result_table_path=sys.argv[4]


def getDepths(df):
    return pd.concat([df[['Hole_ID','from_m']].rename(columns={'from_m':'depth_m'}),
               df[['Hole_ID','to_m']].rename(columns={'to_m':'depth_m'})]).drop_duplicates()

def getAllDepts(ldf):
    return pd.concat([getDepths(_) for _ in ldf]).drop_duplicates().sort_values('depth_m')

def merge_table(master, slave):
    merged_df=pd.merge(master, slave, how='inner', on=['Hole_ID'],suffixes=('', right_suffix))
    merged_df=merged_df[(merged_df['from_m']>=merged_df['from_m%s'%right_suffix]) & 
                     (merged_df['to_m']<=merged_df['to_m%s'%right_suffix])]
    return merged_df.drop(columns=['from_m%s'%right_suffix,'to_m%s'%right_suffix])

def remove_suffix_right(df):
    return df.loc[:, ~df.columns.str.endswith("_right")]

df_master = pd.read_csv(master_table_path).rename(columns={'From_m':'from_m','To_m':'to_m'})
df_slave = pd.read_csv(slave_table_path).rename(columns={'From_m':'from_m','To_m':'to_m'})

all_depths=getAllDepts([df_master,df_slave])
all_depths['to_m']=all_depths.groupby('Hole_ID').shift(-1)['depth_m']

all_depths=all_depths.dropna().rename(columns={'depth_m':'from_m'})

df_merged_1 = remove_suffix_right(merge_table(all_depths, df_master))
df_merged = remove_suffix_right(merge_table(df_merged_1, df_slave))

df_void_dirty = pd.merge(df_merged_1, df_merged, how='outer', on=['Hole_ID', 'from_m', 'to_m'], 
           suffixes=('', '_right'), indicator=True)

df_void_clean = remove_suffix_right(df_void_dirty)
df_void = df_void_clean[df_void_clean['_merge']=='left_only'].drop(columns=['_merge'])

df_result = pd.concat([df_merged,df_void], ignore_index=True).sort_values(['Hole_ID', 'from_m'])

df_result.to_csv(result_table_path, index=False)





# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:28:41 2022

@author: EDUARDO
"""

#%%%%%
#%% prueba de modificacion 3 - branch2
#%% comentario 20220918 v4
#%% mis nuevos cambios fff


from pyathena import connect
import pandas as pd
from tabulate import tabulate

conn = connect(  aws_access_key_id='AKIA52GMK3P66EW6253U',
                 aws_secret_access_key='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',
                 s3_staging_dir="s3://entel-lab/ATHENA_QUERY_OTHERS/",
                 region_name="us-east-1")
                 
def_query = """ select id_periodo , count(1) from glue_dwh_fct_sbsc_mvmn.tb_fct_sbsc_mvmn
where id_periodo not in ('202207')
group by id_periodo 
order by id_periodo desc; """
                 
df = pd.read_sql_query(def_query , conn)
print(tabulate(df, headers='keys', tablefmt='psql'))
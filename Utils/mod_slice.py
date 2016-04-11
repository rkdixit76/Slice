
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import datetime as dt
import os
import re


# In[3]:

# FUNCTIONS

def conv_curr_to_float(df,*bound):   #function for converting currency values to float
    
    df.ix[bound[0]:bound[1],bound[2]:bound[3]]=df.ix[bound[0]:bound[1],bound[2]:bound[3]]    .apply(lambda x: x.str.replace(r'[$,]','').astype(float)) #Convert to numbers
    df.fillna(0,inplace=True)
    

def slice_data(*bound,rdata,hdr_row_idx,drp_hdr_row=False):      # Function for slicing data
    s_data = rdata.ix[bound[0]:bound[1],bound[2]:bound[3]]
    s_data.columns = rdata.ix[hdr_row_idx,bound[2]:bound[3]]
    if(drp_hdr_row):
        s_data.drop(hdr_row_idx,inplace=True)
    s_data.reset_index(inplace=True,drop=True)
    
    return(s_data)

def drp_rows(df,rows): #Drops a row
    df.drop(df.index[rows],inplace=True)
    df.reset_index(inplace=True,drop=True)
    return(df)


# In[7]:

def get_raw_data(fname,rst_col_idx=False,rst_row_idx=False,sht=0):
    f,fext = os.path.splitext(fname)
    
    if fext in ['.csv']:
        df = pd.read_csv(fname)
    elif fext in ['.xls','.xlsx']:
        df = pd.read_excel(fname,sheetname=sht)
    
    if(rst_col_idx): #Reset cols to 0..N indices
        df.columns = np.arange(len(df.columns))
    if(rst_row_idx): #Reset row indices
        df.reset_index(inplace=True,drop=True)
        
    return(df)


# In[4]:

def conv_colidx_datetime(df,frmt): #Returns list containing datetime values wherever possible
    cols = df.columns.tolist()
    col_dt = []
    for item in cols:
        try:
            conv = pd.to_datetime(item.replace(' ',''),format=frmt)
            col_dt.append(conv.date())
        except:
            col_dt.append(item)
    df.columns = col_dt    


# In[2]:

#Convert column to datetime
def conv_str_to_datetime(df,col,str_col=True):
    if(str_col):
        df[col]=pd.to_datetime(df[col])
    else:
        df[col]=df[col].map(lambda x:pd.to_datetime(x) if isinstance(x,str) else x)
    


# In[6]:

def truncate_timestamp_colidx_todate(df):
    for cl in df.columns:
        if type(cl) == dt.datetime:
            cl_date = dt.date(cl.year,cl.month,cl.day)
            df.rename(columns={cl:cl_date},inplace=True)


# In[10]:

#Parses data from complex column
def arg_parser(arg,search_str):
    try:
        pat = '(?<='+search_str+'":)"(.*?)"'
        s = re.search(pat,arg).group(1)
    except:
        s=np.NaN
    
    return(s)

def get_search_cols(data,search_string='',arg_column_name='',ret_cnt=False,to_numeric=True,to_date=False):
    
    sr_col = pd.DataFrame({search_string:data[arg_column_name]                                .apply(lambda x:arg_parser(x,search_string))})
    sr_col.columns = [search_string]
    if to_numeric:
        sr_col[search_string] = pd.to_numeric(sr_col[search_string])
    elif to_date:
        sr_col[search_string] = pd.to_datetime(sr_col[search_string])
    
    if ret_cnt: #Add a count column and return. Helpful for series grouping or dataframes without numeric data
        sr_col['Count'] = np.ones(len(sr_col))
        
    return(sr_col)


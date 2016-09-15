
# coding: utf-8

# In[2]:

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


# In[4]:

def get_raw_data(fname,rst_col_idx=False,rst_row_idx=False,sht=0,pdate=False):
    f,fext = os.path.splitext(fname)
    
    if fext in ['.csv']:
        df = pd.read_csv(fname,low_memory=False,parse_dates=pdate,infer_datetime_format=True)
    elif fext in ['.xls','.xlsx']:
        df = pd.read_excel(fname,sheetname=sht)
    
    if(rst_col_idx): #Reset cols to 0..N indices
        df.columns = np.arange(len(df.columns))
    if(rst_row_idx): #Reset row indices
        df.reset_index(inplace=True,drop=True)
        
    return(df)


# In[5]:

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


# In[6]:

#Convert column to datetime
def conv_str_to_datetime(df,col,str_col=True,conv_to_date=False):
    if(str_col):
        df[col]=pd.to_datetime(df[col])
    else:
        df[col]=df[col].map(lambda x:pd.to_datetime(x) if isinstance(x,str) else x)
    
#     if(conv_to_date):
#         df[col] = df[col].apply(lambda)


# In[7]:

# Convert columns to datetime
def conv_cols_datetime(df,d_cols):
    
    for col in d_cols:
        conv_str_to_datetime(df,col)


# In[8]:

def truncate_timestamp_colidx_todate(df):
    for cl in df.columns:
        if type(cl) == dt.datetime:
            cl_date = dt.date(cl.year,cl.month,cl.day)
            df.rename(columns={cl:cl_date},inplace=True)


# In[9]:

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


# In[10]:

def get_combined_hist_dates(df,dt_colname,dt_range,tgt_colname,grp_colname='user_id',bin_range=np.arange(1,11,1)):
    
    b_range_temp = np.append(bin_range,bin_range[len(bin_range)-1]+1)
    hist_df = pd.DataFrame(np.zeros(len(bin_range)),index=bin_range,columns=['freq'])
    num_records = (dt_range.max()-dt_range.min()).days+1
    for for_date in dt_range:
    
        hist_freq,bin_edges = np.histogram(df[df[dt_colname]==for_date][[grp_colname,tgt_colname]].                             groupby(grp_colname).sum(),bins=b_range_temp)
        hist_df['freq'] = hist_df['freq'] + hist_freq
    hist_df['freq'] = hist_df['freq']/num_records

    return(hist_df)


# In[11]:

def cat_df_cols(df,col_list,obj_cols=False):
    # Converts cols in df to dtype category
    # If obj_cols == True, then all columns with dtype==object will be set to categories
    if(obj_cols):
        col_list = df.dtypes[df.dtypes==object].index
        
    for col in col_list:
        df[col] = df[col].astype('category')


# In[12]:

def save_to_hdfs(fpath,rst_col_idx=False,rst_row_idx=False,sht=0,pdate=False,append=True):
    raw_data = get_raw_data(fpath,rst_col_idx=rst_col_idx,rst_row_idx=rst_row_idx,sht=sht,pdate=pdate)
    hdfs_fp,ext = os.path.splitext(fpath)
    hdfs_fp = hdfs_fp+'.h5'
    raw_data.to_hdf(hdfs_fp,'table',append=append)
    


# In[13]:

def str_to_numeric(df,cols,dtp,replace_strs):
    for col in cols:
        for s in replace_strs:
            df[col] = df[col].replace(s,'',regex=True)
        df[col] = df[col].astype(dtp)


# In[14]:

def conv_cols_float(df,non_flt_cols):
    for col in non_flt_cols:
        df[col]=df[col].astype('float64')


# In[15]:

def frmt_data_dtime_float(df,date_cols,non_float_cols,set_idx=False,set_idx_col=None):
    if(date_cols):
        conv_cols_datetime(df,date_cols)
    if(non_float_cols):
        conv_cols_float(df,non_float_cols)
    cat_df_cols(df,'',obj_cols=True)
    if(set_idx):
        df.set_index(set_idx_col,drop=True,inplace=True)


# In[16]:

def convert_save_df_hdfs(df,dt_cols,non_flt_cols,hdfs_path,set_idx=False,set_idx_colname=None):
    frmt_data_dtime_float(df,dt_cols,non_flt_cols,set_idx,set_idx_colname)
    store = pd.HDFStore(hdfs_path,format='table',mode='w')
    store.append('table',df)
    store.close()


# In[17]:

def get_df_mb(df):
    # Return size in MB of df in memory
    return(df.memory_usage().sum()*1e-6)


# In[18]:

def save_df_to_hdfs(df,hdfs_path):
    store = pd.HDFStore(hdfs_path,format='table',mode='w')
    store.append('table',df)
    store.close()


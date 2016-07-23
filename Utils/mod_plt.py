
# coding: utf-8

# In[5]:

import matplotlib.pyplot as plt
import mod_fitting


# In[6]:

# Defaults for plots
font_title_label = {'family': 'arial',
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }


# In[7]:

def curve_fitplot(*fitparam,xv,yv,lbl,fhandle):
    plt.figure(figsize=(15,7))
    plt.plot(xv,yv,'ko', label=lbl)
    plt.plot(xv,fhandle(xv, *fitparam),'r-', label="Fitted Curve")
    plt.legend()
    plt.grid()


# In[8]:

def single_xy_plot(data_x,data_y,leg_lbl,fsize):
    fig, ax = plt.subplots(figsize=fsize)
    ax.plot(data_x,data_y,label=leg_lbl)
    ax.legend()
    ax.grid()
    


# In[9]:

def dataframe_plot(df,fsize):
    ax = df.plot(grid=True)
    f = ax.get_figure()
    f.set_size_inches(fsize)
    


# In[10]:

def frmt_plot(ttl='',xl='',yl='',fd=font_title_label,fsize=14):
    plt.title(ttl,fontdict=fd)
    plt.xlabel(xl,fontdict=fd)
    plt.ylabel(yl,fontdict=fd)
    plt.legend(fontsize=fsize)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)


# In[11]:

def frmt_axis(ax,ttl='',xl='',yl='',fd=font_title_label,fsize=14):
    ax.set_title(ttl,fontdict=fd)
    ax.set_xlabel(xl,fontdict=fd)
    ax.set_ylabel(yl,fontdict=fd)
    ax.legend(fontsize=fsize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(fsize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(fsize)


# In[6]:

def df_timestamp_todate_plot(df,fsize=(15,7),grid=True,kind='bar',lw=0,alpha=0.7,rot=90):
    # Plot dataframe that has DateTimeIndex as a timestamp. Convert it to date from timestamp
    set_xticks=False
    if (kind=='line'):
        if(lw==0): #Check line width param
            lw=2
        
        set_xticks=True # Set xticks for line plot
        
    ax = df.plot(figsize=fsize,grid=grid,kind=kind,lw=lw,alpha=alpha,rot=rot);
    if(set_xticks):
        ax.set_xticks(df.index.date);
    
    ax.set_xticklabels(df.index.date);
    


# In[1]:

def std_plot(df,figsize=(30,10),pltkind='line',stkd=True,clrs=None,ttl=None,xl=None,yl=None,            conv_xaxis=False,xaxis_frmt='%b-%y',rot=0):
    if (pltkind=='bar' or pltkind=='barh'):
        if(clrs):
            ax=df.plot(kind=pltkind,figsize=figsize,grid=True,lw=0,stacked=stkd,alpha=0.6,color=clrs,legend=True,rot=rot);
        else:
            ax=df.plot(kind=pltkind,figsize=figsize,grid=True,lw=0,stacked=stkd,alpha=0.6,legend=True,rot=rot);
        
        if(conv_xaxis):
            ax.set_xticklabels(df.index.strftime(xaxis_frmt));
   
    elif pltkind=='line':
        df.plot(kind=pltkind,figsize=figsize,grid=True,lw=2,rot=rot);
        
    frmt_plot(ttl=ttl,xl=xl,yl=yl);


# In[6]:

def plt_multiple_df(df_list,legend_list,pltkind='line',figsize=(20,10),location='best',ttl='',xl='',yl=''):
    # Function to plot multiple dataframes on one axis
    if(pltkind=='line'):
        idx=0
        for df in df_list:
            if(idx==0): #First plot
                ax=df.plot(kind=pltkind,figsize=figsize,grid=True,lw=2);
            else:
                df.plot(ax=ax,kind=pltkind,figsize=figsize,grid=True,lw=2);
            idx+=1
    
    frmt_axis(ax,ttl=ttl,xl=xl,yl=yl);
    ax.legend(legend_list,loc=location); #Set the legend



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



# coding: utf-8

# In[6]:

import matplotlib.pyplot as plt
import mod_fitting


# In[7]:

# Defaults for plots
font_title_label = {'family': 'arial',
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }


# In[8]:

def curve_fitplot(*fitparam,xv,yv,lbl):
    plt.figure(figsize=(15,7))
    plt.plot(xv, yv, 'ko', label=lbl)
    plt.plot(xv, mod_fitting.func(xv, *fitparam), 'r-', label="Fitted Curve")
    plt.legend()
    plt.grid()


# In[9]:

def single_xy_plot(data_x,data_y,leg_lbl,fsize):
    fig, ax = plt.subplots(figsize=fsize)
    ax.plot(data_x,data_y,label=leg_lbl)
    ax.legend()
    ax.grid()
    


# In[10]:

def dataframe_plot(df,fsize):
    ax = df.plot(grid=True)
    f = ax.get_figure()
    f.set_size_inches(fsize)
    


# In[11]:

def frmt_plot(ttl='',xl='',yl='',fd=font_title_label,fsize=14):
    plt.title(ttl,fontdict=fd)
    plt.xlabel(xl,fontdict=fd)
    plt.ylabel(yl,fontdict=fd)
    plt.legend(fontsize=fsize)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)


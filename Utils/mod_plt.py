
# coding: utf-8

# In[21]:

import matplotlib.pyplot as plt
import mod_fitting


# In[22]:

def curve_fitplot(*fitparam,xv,yv,lbl):
    plt.figure(figsize=(15,7))
    plt.plot(xv, yv, 'ko', label=lbl)
    plt.plot(xv, mod_fitting.func(xv, *fitparam), 'r-', label="Fitted Curve")
    plt.legend()
    plt.grid()


# In[19]:

def single_xy_plot(data_x,data_y,leg_lbl,fsize):
    fig, ax = plt.subplots(figsize=fsize)
    ax.plot(data_x,data_y,label=leg_lbl)
    ax.legend()
    ax.grid()
    


# In[5]:

def dataframe_plot(df,fsize):
    ax = df.plot(grid=True)
    f = ax.get_figure()
    f.set_size_inches(fsize)
    


# In[1]:

def frmt_plot(ttl='',xl='',yl='',fd='',fsize=14):
    plt.title(ttl,fontdict=fd)
    plt.xlabel(xl,fontdict=fd)
    plt.ylabel(yl,fontdict=fd)
    plt.legend(fontsize=fsize)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)


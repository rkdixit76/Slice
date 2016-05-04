
# coding: utf-8

# In[29]:

from scipy.optimize import curve_fit
import numpy as np
import mod_plt
import importlib


# In[30]:

importlib.reload(mod_plt)


# In[31]:

def func(x, a, b, c):  #For curve fitting
    return a * np.exp(-b * x) + c


# In[32]:

def one_by_x_sq(x,a,b):
    return(a/np.sin((1/(b*x*np.pi/180)**0.5)))


# In[33]:

def curvefit(y,*guess_values,lbl,plt_enable=False,xd_act=np.arange(1,100,1),bnds=([0,0,0],[100,100,100])):
    xd = xd_act
    yd=np.nan_to_num(y.values.astype('float64'))
    
    popt1, pcov1 = curve_fit(func,xd,yd,p0=guess_values,bounds=bnds)
    print('Equation a*e^(-bx)+c Constants [a,b,c]:',popt1)
    
    if(plt_enable):
        mod_plt.curve_fitplot(*popt1,xv=xd,yv=yd,lbl=lbl)
    return((popt1,pcov1))


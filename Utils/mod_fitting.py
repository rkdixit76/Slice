
# coding: utf-8

# In[27]:

from scipy.optimize import curve_fit
import numpy as np
import mod_plt
import importlib


# In[28]:

importlib.reload(mod_plt)


# In[33]:

def func(x, a, b, c):  #For curve fitting
    return a * np.exp(-b * x) + c


# In[32]:

def curvefit(y,*guess_values,lbl,plt_enable=False):
    xd = np.arange(0,len(y),1)
    yd=np.nan_to_num(y.values.astype('float64'))
    
    popt1, pcov1 = curve_fit(func,xd,yd,p0=guess_values,maxfev=2000)
    print('Equation a*e^(-bx)+c Constants [a,b,c]:',popt1)
    
    if(plt_enable):
        mod_plt.curve_fitplot(*popt1,xv=xd,yv=yd,lbl=lbl)
    return((popt1,pcov1))


# In[ ]:





# coding: utf-8

# In[27]:

from scipy.optimize import curve_fit
import numpy as np
import mod_plt
import importlib


# In[28]:

importlib.reload(mod_plt)


# In[29]:

def func(x, a, b, c):  #For curve fitting
    return a * np.exp(-b * x) + c


# In[30]:

def one_by_x_sq(x,a,b):
    return(a/np.sin((1/(b*x*np.pi/180)**0.5)))


# In[31]:

def linear(x,a,b):
    return(a*x+b)


# In[33]:

def poly_2nd(x,a,b,c):
    return(a*(x**2) + b*x + c)


# In[34]:

def exp_growth(x,a,b):
    # y = a*e^(b*x)
    return(a*np.exp(b*x))


# In[32]:

def curvefit(y,*guess_values,lbl,plt_enable=False,xd_act=np.arange(1,100,1),bnds=([0,0,0],[100,100,100]),fhandle=func):
    xd = xd_act
    yd=np.nan_to_num(y.values.astype('float64'))
    
    popt1, pcov1 = curve_fit(fhandle,xdata=xd,ydata=yd,p0=guess_values,bounds=bnds)
    print('Equation coefficients:',popt1)
    
    if(plt_enable):
        mod_plt.curve_fitplot(*popt1,xv=xd,yv=yd,lbl=lbl,fhandle=fhandle)
    return((popt1,pcov1))


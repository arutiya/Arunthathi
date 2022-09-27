# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 00:47:19 2022

@author: Arunthathi
"""
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
iris.head()
iris.describe()
iris.dtypes
iris.columns

SL_new = pd.cut(iris['Sepal.Length'], bins = 2, labels=["Low", "High"]) 
SL = pd.cut(iris['Sepal.Length'],bins=3,right=False) #used for binning

SW_new = pd.cut(iris['Sepal.Width'],bins=3,labels=np.arange(3),right=False)
SW = pd.cut(iris['Sepal.Width'],bins=3,right=False) #used for binning

PL_new = pd.cut(iris['Petal.Length'],bins=4,labels=np.arange(4),right=False)
PL = pd.cut(iris['Petal.Length'],bins=4,right=False) #used for binning

PW_new = pd.cut(iris['Petal.Width'],bins=4,labels=np.arange(4),right=False)
PW = pd.cut(iris['Petal.Width'],bins=4,right=False) #used for binning

iris






























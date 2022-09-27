# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:17:10 2022

@author: Arunthathi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

# outlier treatment

boston.dtypes
plt.boxplot(boston)
# from all thies boxplot we can see that column 'crim','zn','rm', 'dis','black','lstat','medv' has some outlier

# Let's find outliers in crim

######## for "crim" column finding and replacing ##############
# Detection of outliers (find limits for crim based on IQR)
crim_IQR = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)
crim_max = boston['crim'].quantile(0.75) + (IQR * 1.5)  #outliers in maxima side

####################### Replace ############################
# Now let's replace the outliers by the maximum and minimum limit
boston['crim_replaced']= pd.DataFrame(np.where(boston['crim'] > crim_max, crim_max , boston['crim']))
sns.boxplot(boston.crim_replaced);plt.title('Boxplot');plt.show()

######## for "rm" column finding and replacing
sns.boxplot(boston.rm)  #outlier in both sides
# Detection of outliers for rad column(find limits for RM based on IQR)

rm_IQR = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)
rm_lower_limit = boston['rm'].quantile(0.25) - (rm_IQR * 1.5)
rm_upper_limit = boston['rm'].quantile(0.75) + (rm_IQR * 1.5)

####################### Replace ############################
# Now let's replace the outliers by the maximum and minimum limit
boston['rm_replaced']= pd.DataFrame(np.where(boston['rm'] > rm_upper_limit, rm_upper_limit, 
                                         np.where(boston['rm'] < rm_lower_limit, rm_lower_limit, boston['rm'])))
sns.boxplot(boston.rm_replaced);plt.title('Boxplot');plt.show()

######## for "zn" column finding and replacing ##############
sns.boxplot(boston.zn)  #outlier in max side
zn_IQR = boston['zn'].quantile(0.75)-boston['zn'].quantile(0.25)
zn_up_lm= boston['zn'].quantile(0.75)+(zn_IQR*1.5)
###########replacling with upper limit ##########
boston['zn_replaced']=pd.DataFrame(np.where(boston['zn']>zn_up_lm,zn_up_lm, boston['zn']))
sns.boxplot(boston.zn_replaced);plt.title('Boxplot');plt.show()


######## for "dis" column finding and replacing #############
sns.boxplot(boston.dis)  #outlier in max side
dis_IQR=boston['dis'].quantile(0.75)-boston['dis'].quantile(0.25)
dis_up_lm= boston['dis'].quantile(0.75)+(dis_IQR*1.5)
###########replacling with upper limit ##########
boston['dis_replaced']=pd.DataFrame(np.where(boston['dis']>dis_up_lm,dis_up_lm,boston['dis']))
sns.boxplot(boston.dis_replaced);plt.title('Boxplot');plt.show()



######## for "medv" columnfinding and replacing #############
sns.boxplot(boston.medv) #outlier in max side
medv_IQR = boston['medv'].quantile(0.75)-boston['medv'].quantile(0.25)
medv_up_lm=boston['medv'].quantile(0.75)+(medv_IQR*1.5)

###########replacling with upper limit ##########
boston['medv_replaced']=pd.DataFrame(np.where(boston['medv']>medv_up_lm,medv_up_lm,boston['medv']))
sns.boxplot(boston['medv_replaced']);plt.title('Boxplot');plt.show()


######## for "ptratio" column finding and replacing #############
sns.boxplot(boston.ptratio) #outlier in min side
ptr_IQR=boston['ptratio'].quantile(0.75)-boston['ptratio'].quantile(0.25)
ptr_lo_lm=boston['ptratio'].quantile(0.25)  - (ptr_IQR*1.5)

##########replacing ##########################3
boston['ptratio_replaced']=pd.DataFrame(np.where(boston['ptratio']<ptr_lo_lm,ptr_lo_lm,boston['ptratio']))
sns.boxplot(boston['ptratio_replaced']);plt.title('Boxplot');plt.show()


################# for "black" finding and replacing #############
sns.boxplot(boston.black)    # outlier in min side
bla_IQR=boston['black'].quantile(0.75)-boston['black'].quantile(0.25)
bla_lo_lm=boston['black'].quantile(0.25)  - (bla_IQR*1.5)

##########replacing####################
boston['black_replaced']=pd.DataFrame(np.where(boston['black']<bla_lo_lm,bla_lo_lm,boston['black']))
sns.boxplot(boston['black_replaced']);plt.title('Boxplot');plt.show()




























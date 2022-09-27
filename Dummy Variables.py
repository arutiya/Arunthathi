# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 10:12:57 2022

@author: Arunthathi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use the animal_category dataset
animal.columns
animal.shape

#column Index has nothing important 
#removing Index 

animal.drop(animal.columns[0], axis = 1, inplace = True) #now shape is 30*4

animal.dtypes

animal.info()             # data has no na or nall values

##################  creating Dummy variables using dummies ###############
# Create dummy variables on categorcal columns

############ 1 method
animal_new = pd.get_dummies(animal)


###########2 moethod #####################################3

from sklearn.preprocessing import OneHotEncoder

#creating instance fo One Hot Encoder

enc = OneHotEncoder()

enc_animal = pd.DataFrame(enc.fit_transform(animal).toarray())


#############3 method######################################

from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()

animal.columns

animal['Animals']= labelencoder.fit_transform(animal['Animals'])
animal['Gender'] = labelencoder.fit_transform(animal['Gender'])
animal['Homly'] = labelencoder.fit_transform(animal['Homly'])
animal['Types'] = labelencoder.fit_transform(animal['Types'])

























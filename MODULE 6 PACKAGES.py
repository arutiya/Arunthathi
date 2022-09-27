#---------------MODULE 6 PACKAGES------------

# 1.	For the dataset “Indian_cities”, 


import panda as pd

type(cities)

cities

#a)	Find out top 10 states in female-male sex ratio

sex_ratio_values = cities.sort_values(by = "sex_ratio", ascending = False).sex_ratio

sex_ratio_values[0:10] 

# Output:
   # Out[148]: 
    278    1093
    275    1077
    14     1076
    461    1076
    459    1064
    220    1055
    358    1053
    245    1046
    378    1045
    430    1042
    Name: sex_ratio, dtype: int64

sex_ratio = cities.sort_values(by="sex_ratio",ascending = False).name_of_city

sex_ratio[0:10]

#output:
   # Out[150]: 
    278             Kozhikode 
    275                Kollam 
    14              Alappuzha 
    461              Thrissur 
    459    Thiruvananthapuram 
    220                Imphal 
    358              Palakkad 
    245              Kakinada 
    378            Puducherry 
    430              Shillong 
    Name: name_of_city, dtype: object
    


#b)	Find out top 10 cities in total number of graduates

graduates_values = cities.sort_values(by= "total_graduates",ascending = False). total_graduates

graduates_values [0:10]

#output: graduates_values [0:10]
Out[157]: 
141    2221137
185    1802371
72     1591163
184    1164149
119     879695
274     818476
7       769858
380     656508
288     596990
225     533148
Name: total_graduates, dtype: int64

# c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

literacy_values = cities.sort_values(by ="effective_literacy_rate_total",ascending = False).effective_literacy_rate_total

literacy_values [0:10]

#output: 
   # Out[162]: 
    9      98.80
    271    97.49
    461    97.24
    278    96.80
    14     96.56
    264    95.50
    333    95.35
    13     95.15
    352    94.78
    431    94.67
    Name: effective_literacy_rate_total, dtype: float64
    
location_values = cities.sort_values(by ="effective_literacy_rate_total",ascending = False).location

location_values [0:10]  

# Out[166]: 
9       23.727107,92.7176389
271     9.9312328,76.2673041
461    10.5276416,76.2144349
278      11.2587531,75.78041
14      9.4980667,76.3388484
264    22.7002943,88.3753455
333     8.1832857,77.4118996
13     12.9974873,80.2006371
352     22.7902358,88.367179
431    31.1048145,77.1734033
Name: location, dtype: object

#2.	For the data set “Indian_cities”
#a)	Construct histogram on literates_total and comment about the inferences

import matplotlib.pyplot as plt

plt.hist(cities.literates_total)
#histogram is positively scwed i.e mean>median>mode

#there is also persence of Outliers

#b)	Construct scatter  plot between  male graduates and female graduates

plt.scatter(cities.male_graduates, cities.female_graduates)

#3.	For the data set “Indian_cities”
#a)	Construct Boxplot on total effective literacy rate and draw inferences

plt.boxplot(cities.effective_literacy_rate_total)
#distribution is negetively scwed, and there is also persence of outliers

#b)	Find out the number of null values in each column of the dataset and delete them

cities.isna()

cities.dropna()
￼




























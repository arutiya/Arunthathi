# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:17:10 2022

@author: Arunthathi
"""



#------------------------module 2 Operators--------------------------
#Problem 1.A.
x = 12345

y = 543

z = 399 

z > x + y

        Out[32]: False

#Problem 1.B
a = 5

b = 3

c = -5

a//b
Out[37]: 1

c//b
Out[38]: -2
#when we take floor division of negative number it returns Quotient as one higher digit


#--------------------------Problem 2------------------------#
#Problem 2.  a=5,b=3,c=10.. What will be the output of the following:
#            A. a/=b
#            B. c*=5  
a=5
b=3
c=10
# a/=b means a = a/b
# c = c*5
d = 5/3
       #Out[36]: 1.6666666666666667
e = c*5
      #Out[38]: 50
#Problem 3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
#           B. How can you obtain 64 by using numbers 4 and 3 .

#A. we can check alphabet 's' in word "Data Science" using Membership operator
#If output is True then alphabet is present in string; 
#if output is False then alphabet is not present in that string

's' in 'Data Science'       #Out[42]: False
#'s' is not present in "Data Science"
#Python is case sensiive so 's' is not equal to 'S'

#B. we can obtain 64 using 4 and 3 by expoonential operator 
exp = 4**3
print(exp)          #Output 64


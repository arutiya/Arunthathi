# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:17:10 2022

@author: Arunthathi
"""




#-------------MODULE 5 LOOPS and Functions------------------

#1.	
#A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters 
#exists in list1

list1 = [1, 5.5, (10+20j), "data science"]

for i in list1:
    print(i)
    
    #out put: for i in list1:
        print(i)
    1
    5.5
    (10+20j)
    data science
    
#) How do we create a sequence of numbers in Python.

[x for x in range (1,29,3)]

#output:  Out[88]: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

#)  Read the input from keyboard and print a sequence of numbers up to that number
    
num = int(input("Enter a number:- ")) #taking input from keyboard

[x for x in range(1,1+num)]             #printing sequence up to entered number

#2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
#listcontains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#Create a dictionary such that list2 are keys and list 1 are values..


list1 =[x for x in range(1,10)]
list1
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']
list2

dic = {"one":1,"two":2,"three":3,"four" :4,"five":5,"six":6, "saven":7, "eight":8,"nine":9,"ten":10}
dic.keys()

# 3.	 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is odd number in the list1..

list1 = [3,4,5,6,7,8]

for i in list1:
    if i%2==0:
        print(i+10)
    else:
        print(i*5)
        
        #Output: 15
       15
       14
       25
       16
       35
       18
        
 #    .     Write a simple user defined function that greets a person in such a way that :
 #           i) It should accept both name of person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’
 #         Ex: Hello ---xxxx---, How are you  - default message.
  #         Ex: Hello ---xxxx---, --xx your message xx---
  
  def greet(name,b= 'how are you'): #Defining function
    print(name,b)
    
greet('Arunthathi')     #Calling defined function

# output:  
#                       greet('Arunthathi')     #Calling defined function
#                       Arunthathi how are you





















# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:20:58 2020

@author: kolli
"""

#factorial of number 

while True:
    num = int(input("Enter the number:"))
    if(num >-1):
        if num == 0:
            print("The factorial of {} is 1".format(num))
            
        else:
            fact = 1
            for i in range(1,num+1):
                fact = fact*i
            print("The factorial of {} is {}".format(num,fact))
    else:
        print("Enter positive number only ")
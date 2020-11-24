# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:46:03 2020

@author: kolli
"""

while True:
    num = int(input("Enter the number: "))
    
    #to check whether the number is even or odd 
    
    if num %2 == 0 :
        print("The number {} is even".format(num))
        
    elif num%2 !=0:
        if num>1:
            for i in range(2,num):
                if (num%i == 0):
                    print("The number {} is odd".format(num))
                    break
            else:
                print("The number {} is prime".format(num))
                
        else:
            print("please enter the number again:")
    
            

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:57:49 2019

@author: Adithya.Balaji
"""
from decimal import Decimal
# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr) 
    positive =0
    negative= 0
    zero = 0
    for i in arr:
        if(i>0):
            positive += 1
        elif(i<0):
            negative += 1
        elif(i==0):
            zero += 1
    print(round(Decimal(positive/length),6))
    print(round(Decimal(negative/length),6))
    print(round(Decimal(zero/length),6))

a = [-4,3,-9,0,4,1]
plusMinus(a)
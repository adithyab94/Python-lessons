# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:40:47 2019

@author: Adithya.Balaji
"""

"""
reverse array withiut reverse()
"""

def reversearr(arr):
    n = len(arr)
    rev = []
    for i in range(n,0,-1):
        rev.append(i)
    return rev

a = [1,2,3,4,5]
print(reversearr(a))
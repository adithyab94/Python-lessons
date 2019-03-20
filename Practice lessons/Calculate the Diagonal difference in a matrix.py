# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:14:17 2019

@author: Adithya.Balaji
"""
"""
This Program calculates the differnce between two diagonals of a square matrix
"""

def diagonalDifference(arr):
    length = len(arr[0])
    print(length)
    prim = [arr[i][i] for i in range(0,length)]
    sec =  [arr[j][length-j-1] for j in range(0,length)]
    print(sec)
    return abs(sum(prim)-sum(sec))


a = [1, 4, 5],[-5, 8, 9],[-6, 7, 11]

print(diagonalDifference(a))
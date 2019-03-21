# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:30:22 2019

@author: Adithya.Balaji
"""
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example,
Sample Input
1 2 3 4 5
Sample Output
10 14
"""

def miniMaxSum(arr):
    arr.sort()
    tot = sum(arr)
    print((tot - arr[-1]), (tot - arr[0]))

a = [1,2,3,4,5]
miniMaxSum(a)



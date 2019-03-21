# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:15:41 2019

@author: Adithya.Balaji


"""
"""
Print staircase of size n
"""



def staircase(n):
    for stairs in range(1,n + 1):
        print(' ' * (n - stairs) + '#' * stairs)

staircase(6)
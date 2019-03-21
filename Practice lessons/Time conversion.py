# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:38:42 2019

@author: Adithya.Balaji
"""

def timeConversion(s):
    #
    # Write your code here.
    # 
    time = s.strip()
    h, m, s = map(int, time[:-2].split(':'))
    p = time[-2:]
    h = h%12 + (p.upper() == "PM")*12
    return ('%02d:%02d:%02d') % (h, m, s)
    
result = timeConversion("07:05:45PM")
print(result)
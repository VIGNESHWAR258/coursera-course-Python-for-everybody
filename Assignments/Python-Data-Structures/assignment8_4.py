# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:52:41 2019

@author: VIGNESHWAR REDDY
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    lines = line.split()
    for word in lines:
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)

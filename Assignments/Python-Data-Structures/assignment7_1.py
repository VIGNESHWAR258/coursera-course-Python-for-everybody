# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:03:26 2019

@author: VIGNESHWAR REDDY
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
#fh = fh.rstrip()
filecontents = fh.read()
print(filecontents.rstrip().upper())
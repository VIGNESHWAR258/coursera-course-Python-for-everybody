# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:57:44 2019

@author: VIGNESHWAR REDDY
"""

# Use the file name mbox-short.txt as the file name
count = 0
addOfValues = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        colon = line.find(':')
        floatingValue = line[colon + 1 : ]
        floatingValue = float(floatingValue)
        addOfValues = addOfValues + floatingValue
        count = count + 1
  
average = addOfValues/count
print('Average spam confidence:',average)
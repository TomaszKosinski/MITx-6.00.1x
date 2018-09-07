#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'abcdefghijklmnopqrstuvwxyz'
maxLen = 1
maxBeginning = 0

for i in range(len(s)):
    print(s[i])
    currentMax = 1
    currentBeginning = i
    for j in range( i+1, len(s)):
        if s[j-1] > s[j] :
            break
        currentMax += 1
    if currentMax > maxLen:
        maxLen = currentMax
        maxBeginning = currentBeginning

result = ""
for i in range( maxLen ):
    result += s[maxBeginning + i]
print ("Longest substring in alphabetical order is: " + result)


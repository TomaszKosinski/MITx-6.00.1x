#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:45:15 2018

@author: tomasz.kosinski
"""

s = 'azcbobobegghakl'
vowels = 'aeiou'
numberOfVowels = 0

for letter in s:
    for vowel in vowels:
        if letter == vowel:
            numberOfVowels = numberOfVowels + 1
            break
print( "Number of vowels: " + str(numberOfVowels) )
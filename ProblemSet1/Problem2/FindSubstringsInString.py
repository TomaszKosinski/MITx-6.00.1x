#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'azcbobobegghakl'
numberOfBobs = 0
bob = "bob"

for i in range( len(s) -2 ):
    for j in range ( len (bob) ):
        if ( s[i+j] != bob[j] ):
            break
        if (j == len(bob) - 1):
            numberOfBobs += 1 

print( "Number of times bob occurs is: " + str(numberOfBobs) )
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = 0
    if a < b:
        testValue = a
    else:
        testValue = b
        
    while testValue > 1 :
        if a % testValue == 0 and b % testValue == 0:
            break
        testValue -= 1 
    return testValue
     
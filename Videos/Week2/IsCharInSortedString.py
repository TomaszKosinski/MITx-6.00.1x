#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return aStr[0] == char
    
    middleIndex = len(aStr)//2 
    if aStr[middleIndex] == char:
        return True
    elif aStr[middleIndex] < char:
        return isIn(char, aStr[middleIndex:])
    else:
        return isIn(char, aStr[0:middleIndex])
    return True
    

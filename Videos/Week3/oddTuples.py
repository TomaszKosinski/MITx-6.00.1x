# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[0::2]

myTuple = ('I', 'am', 'a', 'test', 'tuple')
retTuple = oddTuples(myTuple)
print(retTuple)
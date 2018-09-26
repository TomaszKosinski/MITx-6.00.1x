#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:52:00 2018

@author: tomasz.kosinski
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = string.ascii_lowercase
    
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, "")
    return availableLetters
      
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
print("abcdfghjlmnoqtuvwxyz")
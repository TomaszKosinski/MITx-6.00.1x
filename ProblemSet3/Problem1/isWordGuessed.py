#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:22:52 2018

@author: tomasz
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in lettersGuessed:
        secretWord = secretWord.replace(letter, "")
    if len(secretWord) == 0:
        return True
    return False
    
print("Expected: False True")
print("Got:")
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

secretWord = "ekiprsie"
print(isWordGuessed(secretWord, lettersGuessed))
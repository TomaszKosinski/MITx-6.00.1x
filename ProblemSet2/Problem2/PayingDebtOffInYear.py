#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:31:30 2018

@author: tomasz
"""

def minMonthlyPayment():
    balance = 385
    annualInterestRate = 0.2
 
    minMonthlyPaymentGuess = round((balance // 120)) * 10 - 10
    
    while (True):
        currentBalance = balance
        for month in range(12):
            currentBalance -= minMonthlyPaymentGuess
            currentBalance += currentBalance * annualInterestRate / 12
        if currentBalance < 0:
            break;
        else:
            minMonthlyPaymentGuess += 10 
    print("Lowest Payment: " + str(minMonthlyPaymentGuess))   #310

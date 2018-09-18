#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:31:30 2018

@author: tomasz
"""

def calculateBalanceAfterYear(monthlyPayment, balance, annualInterestRate):
    currentBalance = balance
    for month in range(12):
        currentBalance -= monthlyPayment
        currentBalance += currentBalance * annualInterestRate / 12.0
    return round(currentBalance, 2)

def minMonthlyPayment():
    balance = 320000
    annualInterestRate = 0.2
    # we have to pay at least this (probably more)
    lowerBoundPayment = round(balance / 12.0, 2)
    # we have to pay at most this (probably less)
    upperBoundPayment = round(balance * ((1 + (annualInterestRate/12))**12) / 12.0, 2) 
    
    while (True):
        currentGuess = ( upperBoundPayment + lowerBoundPayment ) / 2.0
        retBalance = calculateBalanceAfterYear(currentGuess, balance, annualInterestRate)
        if(upperBoundPayment - lowerBoundPayment <= 0.01):
            print("Lowest Payment: " + str(round(upperBoundPayment, 2)))
            break
        elif retBalance == 0:
            print("Lowest Payment: " + str(retBalance))
            break
        elif retBalance < 0:
            lowerBoundPayment = currentGuess
        else :
            upperBoundPayment = currentGuess


minMonthlyPayment()    
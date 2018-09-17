#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:31:30 2018

@author: tomasz
"""

def calculateBalanceAfterYear():
    balance = 42
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    
    for month in range(12):
        MinMonthlyPayment = monthlyPaymentRate * balance
        balance -= MinMonthlyPayment
        balance += balance * annualInterestRate / 12
    print("Remaining balance: " + str(round(balance, 2)))

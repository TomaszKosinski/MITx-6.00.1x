#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:52:48 2018

@author: tomasz

Have the generator keep a list of the primes it's generated.
A candidate number x is prime if (x % p) != 0 for all earlier primes p.
"""

def genPrimes():
    primes = [2,]
    index = 0
    
    while True:
        lastPrime = primes[len(primes)-1] 
        yield lastPrime
        candidate = lastPrime + 1
        while True:
            isPrime = True
            for p in primes:
                if candidate % p == 0:
                    candidate +=1
                    isPrime = False
                    break
            if isPrime:
                primes.append(candidate)
                break
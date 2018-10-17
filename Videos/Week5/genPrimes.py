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
            print('Candidate:' + str(candidate))
            print(primes)

            for prime in primes:
                print('Primes ' + str(prime))
                if candidate % prime == 0:
                    print('zwiekszamy dla candidate='+str(candidate) + ' prime:' + str(prime))
                    candidate +=1
                    break
            print("append: " + str(candidate))
            primes.append(candidate)
            break
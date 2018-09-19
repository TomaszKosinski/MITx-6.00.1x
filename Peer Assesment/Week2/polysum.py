#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:53:39 2018

@author: tomasz
"""
import math

def polysum(n, s):
    """
    Input: n, number of sides [int]
    Input: s, length of each side [int/float]
    Returns sum the area and square of the perimeter of the regular polygon (rounded to 4 decimal)
    """
    
    retValue = 0
    perimeter = n * s
    area = 0.25 * n * (s ** 2) / math.tan (math.pi/n)
    retValue = area + perimeter ** 2
    return round(retValue, 4)
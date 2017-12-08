#!/usr/bin/env python

"""
"""

import numpy.random as rnd

def rand_in_range(max): # returns integer, max: integer
    return rnd.randint(max)

def rand_un(): # returns floating point
    return rnd.uniform()

def rand_norm (mu, sigma): # returns floating point, mu: floating point, sigma: floating point
    return rnd.normal(mu, sigma)
    

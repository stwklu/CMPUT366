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
    
def randInRange(max): # returns integer, max: integer # added for backwards combatibility; same as rand_in_range above
    return rnd.randint(max)
    
def randn (mu, sigma): # returns floating point, mu: floating point, sigma: floating point # added for backwards combatibility; same as rand_norm above
    return rnd.normal(mu, sigma)

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Print the fist prime number after the given one


import is_primeDef


def first_prime(a, b):  # Return the 1st prime of the range [a,b]
    p = 0
    for i in range(a, b):
        if is_primeDef.is_prime(i):
            p = i
            break
    return(p)


def first_prime_after(a):
    p = first_prime(a + 1, a + 1000)
    if (p == 0):
        p = first_prime_after(a + 100)
    return(p)

print(first_prime_after(100000000))

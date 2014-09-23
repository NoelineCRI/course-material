# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Print every prime numbers in a range


import is_primeDef


def first_prime(a, b):  # Return the 1st prime of the range [a,b]
    p = 0
    for i in range(a, b):
        if is_primeDef.is_prime(i):
            p = i
            break
    return(p)

l_prime = ""
l_prime += str(first_prime(10000, 10050))
for j in range(first_prime(10000, 10050) + 1, 10050):
    if is_primeDef.is_prime(j):
        l_prime += ", "
        l_prime += str(j)
print(l_prime)

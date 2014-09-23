# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Print the sum of every prime number < 1000


def is_prime(n):
    prime = True
    for i in range(2, n):
        if (n % i) == 0:
            prime = False
            break
    return(prime)

sum = 0
for j in range(2, 1000):
    if is_prime(j):
        # print(j)
        sum += j
print(sum)

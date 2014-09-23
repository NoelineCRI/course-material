# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Check if its given number is a prime one


def is_prime(n):
    if n < 2:
        prime = False
    else:
        prime = True
        for i in range(2, n):
            if (n % i) == 0:
                prime = False
                # print(n,"est divisible par",i)
                break
            # else:
                # print(n,"n'est pas divisible par",i)
    return(prime)

# if prime:
#     print("It is a prime number!")
# else:
#     print("It isn't a prime number")

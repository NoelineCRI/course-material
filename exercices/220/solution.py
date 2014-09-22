# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

#heck if its given number is a prime one

def is_prime(n):
    prime = True
    for i in range(2,n):
        if (n%i)== 0 :
            prime= False
            #print(n,"est divisible par",i)
            break
        #else:
            #print(n,"n'est pas divisible par",i)
    return(prime)

def first_prime(a,b):
    p= 0
    for i in range(a,b):
        if is_prime(i):
            p = i
            break
    return(i)

l_prime=""
l_prime += str(first_prime(10000,10050))
for j in range(first_prime(10000,10050)+1,10050):
    if is_prime(j):
        l_prime +=", "
        l_prime += str(j)
print(l_prime)
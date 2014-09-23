# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Print the head of the fibonacci sequence


def fib(n):
    if n == 0:
        return(1)
    elif n == 1:
        return(1)
    else:
        res = 1
        r2 = 1
        temp = 0
        for i in range(2, n+1):
            temp = res
            res += r2
            r2 = temp
        return(res)


def fib_to(n):
    seq_fib = "" + str(fib(1))
    for i in range(2, n + 1):
        seq_fib += ", "
        seq_fib += str(fib(i))
    seq_fib += "."
    return(seq_fib)

print(fib_to(10))

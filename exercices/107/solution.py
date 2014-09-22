# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a function sets_diff(A, B) that takes to sets in parameters and return all the unique values containes in A and not B.

def sets_diff(A,B):
    for v in A:
        if v not in B:
            print(v)

sets_diff([1,2,3,4,5,6,7],[1,8,9,3])
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a function sets_diff(A, B) that takes to sets in parameters and return all the unique values containes in A and not B.

def sets_union(A,B):
    return(A | B)

a = sets_union(set([1,2,3,4,5,6,7]),set([1,8,9,3]))
print(a)
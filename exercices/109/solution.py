# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a function sets_common([A,B,...]) that take a list of set in parameters and return a set of the commmon values shared by every sets.

def sets_intersection(List):
    finalSet= set(List[0])
    for i in range(1,len(List)):
        finalSet = finalSet & List[i]
    return(finalSet)

print(sets_intersection([set([1,2,3,4,5,6,7]),set([1,8,9,3]),set([3,1,6])]))

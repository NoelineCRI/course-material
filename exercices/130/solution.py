# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

#write a function javanese(A,B) that replace every vowels of a string A with the character set in B and print the result
#See how to replace a character using re module

#Your function javanese("mister tralalilaleler", "o") should return mister trolololololor

#The sentence should be replaced by more that a character

def javanese(A,B):
    newS=""
    for c in A:
        if c in "aeiou":
            newS += B
        else:
            newS += c
    print(newS)


javanese("mister tralalilaleler", "o")
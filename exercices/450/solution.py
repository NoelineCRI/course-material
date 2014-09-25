# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Caesar Cypher

from string import ascii_lowercase
from string import ascii_uppercase
ascii_L = list(ascii_lowercase)
ascii_U = list(ascii_uppercase)
# print(ascii_l)

forward = 1
backward = 0


def caesar_cypher(s, key, method):
    k = key % 26
    res = ""
    for c in s:
        if c in ascii_L:  # Si le char est une lettre min.
            rank_init = ord(c)-97
            if (method == 1):
                rank_f = (rank_init + k) % 26
                res += ascii_L[rank_f]
            elif (method == 0):
                rank_f = (rank_init - k) % 26
                res += ascii_L[rank_f]
            else:
                print("usage : method = backward or forward")
                break

        elif c in ascii_U:  # Si le char est une lettre maj.
            rank_init = ord(c)-ord('A')
            if (method == 1):
                rank_f = (rank_init + k) % 26
                res += ascii_U[rank_f]
            elif (method == 0):
                rank_f = (rank_init - k) % 26
                res += ascii_U[rank_f]
            else:
                print("usage : method = backward or forward")
                break
        else:  # le char n'est pas une lettre : on le garde tel quel
            res += c
    return(res)

# caesar_cypher("Python is super disco !", 31, forward)

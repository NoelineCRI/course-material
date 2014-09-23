# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Draw N Squares


def draw_n_squares(n):
    line1 = "---+" * n
    line2 = "   |" * n
    final_square = ""
    for i in range(n):
        final_square += ("+" + line1+"\n")
        final_square += ("|" + line2+"\n")
    final_square += ("+" + line1)
    return(final_square)

# print(draw_n_squares(5))

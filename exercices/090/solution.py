# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 09:51:30 2014

@author: nono
"""
import sys
l = list(enumerate(sys.argv))
for i in range(len(l)):
    print(l[i][0],l[i][1])
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:31:54 2014

@author: nono
"""

import sys

n1 = 0
n2 = 0

if len(sys.argv) == 4:
    if ((sys.argv[1]).isdigit() and (sys.argv[3]).isdigit() and
            sys.argv[2] in "+-*/%^"):
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[3])
        if sys.argv[2] == "+":
            print(n1 + n2)
        elif sys.argv[2] == "-":
            print(n1 - n2)
        elif sys.argv[2] == "*":
            print(n1 * n2)
        elif (sys.argv[2] == "/" and n2 != 0):
            print(n1 / n2)
        elif (sys.argv[2] == "%" and n2 != 0):
            print(n1 % n2)
        elif sys.argv[2] == "^":
            print(n1 ^ n2)
        else:
            print("usage: python", sys.argv[0],
                  "a_number (an_operator +-*/%^) a_number")
    else:
        print("usage: python", sys.argv[0],
              "a_number (an_operator +-*/%^) a_number")
else:
    print("usage: python", sys.argv[0],
          "a_number (an_operator +-*/%^) a_number")

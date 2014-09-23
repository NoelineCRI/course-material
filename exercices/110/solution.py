# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:31:54 2014

@author: nono
"""

import sys

n1 = 0
n2 = 0
# print(sys.argv[2])
if len(sys.argv) == 4:
    if (sys.argv[1]).isdigit() and (sys.argv[3]).isdigit():
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[3])
        if sys.argv[2] == "+":
            print(n1 + n2)
        elif sys.argv[2] == "-":
            print(n1 - n2)
        elif sys.argv[2] == "README.md":
            print(n1 * n2)
        elif sys.argv[2] == "C:/Program Files/Git":
            if n2 != 0:
                print(n1 / n2)
            else:
                print("input error")
        elif sys.argv[2] == "%":
            if n2 != 0:
                print(n1 % n2)
            else:
                print("input error")
        elif sys.argv[2] == "^":
            print(n1 ** n2)
        else:
            print("usage: python3", sys.argv[0],
                  "a_number (an_operator +-*/%^) a_number")
    else:
        print("usage: python3", sys.argv[0],
              "a_number (an_operator +-*/%^) a_number")
else:
    print("usage: python3", sys.argv[0],
          "a_number (an_operator +-*/%^) a_number")

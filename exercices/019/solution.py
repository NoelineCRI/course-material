# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import sys
if len(sys.argv)>2:
    a = int(float(sys.argv[1]))
    b = int(float(sys.argv[2]))
    print(a+b)
else:
    print("usage: python",sys.argv[0],"OP1 OP2")
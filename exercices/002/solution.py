# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = ""
for w in alphabet:
    if w in "aeiou":
        alphabet2 = w.upper()+ alphabet2
    else:
        alphabet2 = w + alphabet2
print(alphabet2)
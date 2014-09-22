# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a program solution.py that takes a dictionnary and return a list of its keys one by line

def print_dico_Keys(d):
    print("[")
    for k in d.keys():
        print(k)
    print("]")


station = {
 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901
}
print_dico_Keys(station)
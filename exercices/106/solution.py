# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a function my_dicosearch(dictionnary, value) that print a list of all the keys in which values correspond to value.

    
def  my_dicosearch(dictionnary, value):
    print("[")
    for k in dictionnary.keys():
        if dictionnary[k]==value:
            print(k)
    print("]")



station = {
 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901
}
my_dicosearch(station, 31705)
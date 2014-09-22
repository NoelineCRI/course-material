# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:03 2014

@author: nono
"""

#Write a function in a solution.py that take a dictionnary and prints all the ke$ such as :



    
def my_dicolist(dictionnary, v):
    print("[")
    count = 0 
    for k in dictionnary.keys():
        if count < v:
            print(k)
            count += 1
    print("]")



station = {
 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901
}
my_dicolist(station, 3)
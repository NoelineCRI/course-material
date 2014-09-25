# -*- coding: utf-8 -*-

# Give the frequency of letters in the 'words' file

from string import ascii_lowercase
from string import ascii_uppercase
alphaB = list(ascii_lowercase) + list(ascii_uppercase)


def count_let(a):
    f = open('words', 'r')
    count = 0
    l = f.read()
    for w in l:
        if w == a:
            count += 1
    f.close()
    return(count)


f = open('words', 'r')
letters = {}
count_tot = 0
l = f.read()
for w in l:
    if w in alphaB:
        if w not in letters.keys():
            letters[w] = 1
        else:
            letters[w] += 1
        count_tot += 1
for w in letters.keys():
    letters[w] = "%.2f" % (letters[w] / count_tot)
# "%.2f" % permet de couper le nombre à 2 décimales
for a in letters.keys():
    print(a, ":", letters[a])

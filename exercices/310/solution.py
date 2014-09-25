# -*- coding: utf-8 -*-

# Count the lower 'e' in the file 'words'

f = open('words', 'r')
count = 0
for line in f:
    l = f.readline()
    for w in l:
        if w == 'e':
            count += 1
print(count)

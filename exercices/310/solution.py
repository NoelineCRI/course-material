# -*- coding: utf-8 -*-

# Count the lower 'e' in the file 'words'

f = open('words', 'r')
count = 0
for line in f:
    for w in line:
        if w == 'e':
            count += 1
print(count)

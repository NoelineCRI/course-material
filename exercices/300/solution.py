# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:16:14 2014

@author: nono
"""

# Print the content of the file 'words


def print_file_content(file_name):
    f = open(file_name)
    for line in f:
        print(line, end='')

print_file_content('words')

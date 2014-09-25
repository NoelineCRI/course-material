# -*- coding: utf-8 -*-

# euclidean(a, b)
# return the euclidean distance between 2 points a and b with 3 dfrt methods
import numpy as np
import math


def euclidean(a, b):
    res = 0
    for i in range(len(a)):
        res += ((b[i] - a[i]) ** 2)
    return(res ** 0.5)

# print(euclidean([2, 3], [5, 6]))


def opt_euclidean(a, b):  # use of the math module
    res = []
    for i in range(len(a)):
        res = res + [math.pow((b[i] - a[i]), 2)]
    return(math.sqrt(sum(res)))

# print(opt_euclidean([2, 3], [5, 6]))


def np_euclidean(a, b):  # use of the numphy module
    sub = []  # array of the substraction of each dimenstion of the 2 points
    for i in range(np.size(a)):
        sub += [b[i] - a[i]]
    res = np.power(sub, 2)
    return(np.sqrt(res.sum()))

# print(np_euclidean([2, 3], [5, 6]))

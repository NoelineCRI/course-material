# -*- coding: utf-8 -*-

# starts_with
# return true if A begins with B


def start_with(A, B):  # A,B string
    res = True
    for i in range(len(B)):
        if B[i] != A[i]:
            res = False
            break
    return res

# print(start_with("Bonjour toi!", "Bonjour"))

# -*- coding: utf-8 -*-

# starts_with
# return true if A begins with B


def starts_with(A, B):  # A,B string
    # print(len(A))
    # print(len(B))
    if (len(B) > len(A)):
        return False
    else:
        res = True
        for i in range(len(B)):
            if B[i] != A[i]:
                res = False
                break
        return res

# print(starts_with("Bonjour", "Bonjour"))

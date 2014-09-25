# -*- coding: utf-8 -*-

# is_alpha
# return is the string is composed only of letters


def is_alpha(s):  # s is always a string
    from string import ascii_lowercase
    from string import ascii_uppercase
    alphaB = list(ascii_lowercase)+list(ascii_uppercase)
    # print(alphaB)
    res = True
    for w in s:
        if w not in alphaB:
            res = False
            break
    return(res)

# print(is_alpha("abdfebilkngrel bn"))

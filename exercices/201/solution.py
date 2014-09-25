# -*- coding: utf-8 -*-

# is_alpha


def is_alpha(s):  # s is always a string
    from string import ascii_lowercase
    from string import ascii_uppercase
    alphaB = list(ascii_lowercase)+list(ascii_uppercase)
    # print(alphaB)
    res = False
    for w in s:
        if w in alphaB:
            res = True
            break
    return(res)

# print(is_alpha("123'0T234567887659,?"))

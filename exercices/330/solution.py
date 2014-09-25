# -*- coding: utf-8 -*-

# Largest product in a series
f = open('digit', 'r')
numbers = f.read()


def mult13(index_beg):
    res = 1
    for i in range(index_beg, index_beg + 13):
        # print(res, "*", int(numbers[i]))
        res *= int(numbers[i])
    return(res)


def plus_gd13(N):
    plus_gd_res = mult13(0)
    res_courant = plus_gd_res
    for i in range(13, len(N)):
        if int(N[i - 13]) != 0:
            res_courant / int(N[i - 13])
            res_courant *= int(N[i])
            print("res courant :", res_courant)
        else:
            res_courant = mult13(i-12)
            print("res courant :", res_courant)
        if res_courant > plus_gd_res:
            print("nv plus_gd res:", res_courant)
            plus_gd_res = res_courant
            print("plus gd_res : ", plus_gd_res)
    return(plus_gd_res)

# print("Résulat:", plus_gd13(numbers))
res = 0
for i in range(len(numbers)-13):
    res_courant = mult13(i)
    if res_courant > res:
        res = res_courant
        # print("new res", res)
print(res)

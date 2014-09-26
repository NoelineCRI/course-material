# -*- coding: utf-8 -*-

# clean_my_dataset: Json reading and writing

import json

f = open('velib.json', 'r')
list_dico = json.load(f)  # renvoie liste contenue ds le fichier
# help(list_dico)
# print(list_dico[0])

newL = []

for d in list_dico:
    # print(d)
    newD = {}
    newAd = d["address"].split("- ")[0]
    temp = d["address"].split("- ")[1]
    zipC = temp.split(" ")[0]
    city = temp.split(" ")[1]
    name = d["name"].split(" - ")[1]
    # print(name)
    # print(newAd)
    # print(city)
    # print(zipC)
    newD["zipcode"] = zipC
    newD["city"] = city
    newD["address"] = newAd
    newD["name"] = name
    # print(newD)
    newL += [newD]
    # print(newL)

new_f = open('solution.json', 'w')
json.dump(newL, new_f)

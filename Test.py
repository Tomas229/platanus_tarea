import requests
import json
import random


type_dict = {}
for i in range(1, 19):
    type_i = json.loads(requests.get(
        "https://pokeapi.co/api/v2/type/"+str(i)).text)
    type_dict[type_i["name"]] = type_i

for i in type_dict["grass"]["damage_relations"]["double_damage_from"]:
    if i["name"] == "fire":
        weakness_1 = 2


i = 2

import requests
import json


type_dict = {}
for i in range(1, 19):
    type_i = json.loads(requests.get(
        "https://pokeapi.co/api/v2/type/"+str(i)).text)
    type_dict[type_i["name"]] = type_i


print("hola")

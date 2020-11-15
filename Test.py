import requests
import json
import random

type_dict = {}
i = 1
while(True):
    req = requests.get("https://pokeapi.co/api/v2/type/"+str(i))
    if(req.status_code == 404):
        break
    type_i = json.loads(req.text)
    type_dict[type_i["name"]] = type_i
    i += 1


i = 2

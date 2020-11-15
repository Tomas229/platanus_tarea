import requests
import json


type_dict = {}
for i in range(1, 19):
    type_i = json.loads(requests.get(
        "https://pokeapi.co/api/v2/type/"+str(i)).text)
    type_dict[type_i["name"]] = type_i


class Pokemon:
    def __init__(self, id):
        # Preprocessing
        poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
        poke_dict = res = json.loads(poke_req.text)
        # Species
        self.name = poke_dict["species"]["name"]
        # Types
        self.type_1 = poke_dict["types"][0]["type"]["name"]
        self.type_2 = poke_dict["types"][1]["type"]["name"]
        # Stats
        self.hp = poke_dict["stats"][0]["base_stat"]
        self.attack = poke_dict["stats"][1]["base_stat"]
        self.defense = poke_dict["stats"][2]["base_stat"]
        self.special_attack = poke_dict["stats"][3]["base_stat"]
        self.special_defense = poke_dict["stats"][4]["base_stat"]
        self.speed = poke_dict["stats"][5]["base_stat"]
        # Vars
        self.health = self.hp

    def inflict_damage(self, enemy):
        enemy.damage(self.attack)

    def receive_damage(self, value, type):
        mult = 1
        self.hp = self.hp - value*mult

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


class Pokemon:
    def __init__(self, id):
        # Preprocessing
        poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
        poke_dict = json.loads(poke_req.text)
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
        if(self.health <= 0):
            return
        val = max(self.attack, self.special_attack)
        enemy.receive_damage(val, self.type_1)

    def receive_damage(self, value, mov_type):
        damage = max(value - max(self.special_defense, self.defense), 1)

        random_mult = random.randrange(10, 20, 1)/10.0

        self.hp = max(self.hp - damage *
                      self.multiplier_damage(mov_type)*random_mult, 0)

    def multiplier_damage(self, mov_type):
        weakness_1 = 1
        for i in type_dict[self.type_1]["damage_relations"]["double_damage_from"]:
            if i["name"] == self.type_1:
                weakness_1 = 2

        resistance_1 = 1
        for i in type_dict[self.type_1]["damage_relations"]["half_damage_from"]:
            if i["name"] == self.type_1:
                resistance_1 = 0.5

        no_damage_1 = 1
        for i in type_dict[self.type_1]["damage_relations"]["no_damage_from"]:
            if i["name"] == self.type_1:
                no_damage_1 = 0

        weakness_2 = 1
        for i in type_dict[self.type_2]["damage_relations"]["double_damage_from"]:
            if i["name"] == self.type_2:
                weakness_2 = 2

        resistance_2 = 1
        for i in type_dict[self.type_2]["damage_relations"]["half_damage_from"]:
            if i["name"] == self.type_2:
                resistance_2 = 0.5

        no_damage_2 = 1
        for i in type_dict[self.type_2]["damage_relations"]["no_damage_from"]:
            if i["name"] == self.type_2:
                no_damage_2 = 0

        return weakness_1*weakness_2*resistance_1*resistance_2*no_damage_1*no_damage_2

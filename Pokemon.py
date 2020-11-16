import requests
import json
import random

# Global variables
# Type dict is a dictionary that contains all the pokemon types in the games
# Key: Type name ; Value = type info
type_dict = {}

i = 1
while(True):
    req = requests.get("https://pokeapi.co/api/v2/type/"+str(i))
    if(req.status_code == 404):
        break
    type_i = json.loads(req.text)
    type_dict[type_i["name"]] = type_i
    i += 1

# Pokemon class
# Represents a pokemon and its stats
# name: str   the pokemon species
# types: list[str] the pokemon types, pokemon have 1 or 2 types
# hp: int determines a pokemon max health
# attack: int           is used to do damage
# defense: int          is used to do damage
# special_attack: int   is used to reduce damage
# special_defense: int  is used to reduce damage
# speed: int            is used to determine wich pokemon attacks first
# health: int           current pokemon health


class Pokemon:
    def __init__(self, id):
        # Preprocessing
        poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
        poke_dict = json.loads(poke_req.text)
        # Species
        self.name = poke_dict["species"]["name"].capitalize()
        # Types
        self.types = []
        for i in range(len(poke_dict["types"])):
            self.types += [poke_dict["types"][i]["type"]["name"]]
        # Stats
        self.hp = poke_dict["stats"][0]["base_stat"]
        self.attack = poke_dict["stats"][1]["base_stat"]
        self.defense = poke_dict["stats"][2]["base_stat"]
        self.special_attack = poke_dict["stats"][3]["base_stat"]
        self.special_defense = poke_dict["stats"][4]["base_stat"]
        self.speed = poke_dict["stats"][5]["base_stat"]
        # Vars
        self.health = self.hp

    # inflict_damage: Pokemon -> void
    # attacks an enemy pokemon reducing its hp
    # a pokemon can't keep battling if its health drops to zero
    def inflict_damage(self, enemy):
        if(self.health <= 0):
            return
        print(self.name+" attacks")
        val = max(self.attack, self.special_attack)
        enemy.receive_damage(val, self.types[0])

    # receive_damage: int str -> void
    # recieves damage equals to value that's mov_type type
    # reducing the pokemon's health at least in one
    def receive_damage(self, value, mov_type):
        damage = max(value - max(self.special_defense, self.defense), 1)

        random_mult = random.randrange(10, 20, 1)/10.0

        final_damage = max(
            damage * self.multiplier_damage(mov_type)*random_mult, 1)

        self.health = max(self.health - final_damage, 0)

        # flavor text
        print(self.name + " fainted") if self.health <= 0 else None

    # multiplier_damage: str -> int
    # returns the damage multiplier for type effectiveness
    # of mov_type damage

    def multiplier_damage(self, mov_type):
        mult = 1
        for i in range(len(self.types)):  # iterates in the pokemon types
            # Iterates in the weakness, resistances and immunities of the type
            # searching if move_type is in there

            for j in type_dict[self.types[i]]["damage_relations"]["double_damage_from"]:
                if j["name"] == mov_type:
                    mult = mult * 2

            for j in type_dict[self.types[i]]["damage_relations"]["half_damage_from"]:
                if j["name"] == mov_type:
                    mult = mult * 0.5

            for j in type_dict[self.types[i]]["damage_relations"]["no_damage_from"]:
                if j["name"] == mov_type:
                    mult = mult * 0

        # Flavor text
        if(mult > 1):
            print("It's super effective!!!")
        elif(mult == 0):
            print("Barely does damage...")
        elif(mult < 1):
            print("It's not very efective")

        return mult

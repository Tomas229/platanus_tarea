import requests
import json
import random
import Pokemon
import Tournament

# Pokemon tests
pikachu = Pokemon.Pokemon(25)
torterra = Pokemon.Pokemon(389)

# Variables
assert pikachu.name == "Pikachu"
assert torterra.name == "Torterra"

assert pikachu.types == ["electric"]
assert torterra.types == ["grass", "ground"]

assert pikachu.hp == 35
assert pikachu.attack == 55
assert pikachu.defense == 40
assert pikachu.special_attack == 50
assert pikachu.special_defense == 50
assert pikachu.speed == 90
assert pikachu.health == 35

assert torterra.hp == 95
assert torterra.attack == 109
assert torterra.defense == 105
assert torterra.special_attack == 75
assert torterra.special_defense == 85
assert torterra.speed == 56
assert torterra.health == 95

# methods
pikachu.inflict_damage(torterra)
print("Done")

Tournament.begin_tournament(Tournament.make_tournament(8))

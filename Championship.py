import Pokemon
import random

participants = []


def ChampionshipEntry():
    id = random.randrange(152)
    if(id == 0):
        id = 389
    return Pokemon.Pokemon(id)

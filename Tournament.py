import Pokemon
import random

# make_tournament: int -> list[Pokemon]
# returns the list that contains n pokemon
# that will be part of the tournament
# these pokemon will be chosen at random.
# n must be a power of 2


def make_tournament(n):
    participants = []
    for i in range(n):
        id = random.randrange(152)
        if(id == 0):
            id = 389  # Torterra
        participants += [Pokemon.Pokemon(id)]

    # flavor text
    print("The contestants for this tournament are:")
    for i in participants:
        print(i.name)

    return participants

# battle: Pokemon Pokemon -> Pokemon
# starts combat between two pokemon
# until the health of one of them drops to zero
# and returns the winner


def battle(pokemon1, pokemon2):
    print(pokemon1.name + " vs " + pokemon2.name)
    winner = None
    while(pokemon1.health > 0 and pokemon2.health > 0):
        if(pokemon1.speed > pokemon2.speed):
            print(pokemon1.name+" attacks")
            pokemon1.inflict_damage(pokemon2)
            print(pokemon2.name+" attacks")
            pokemon2.inflict_damage(pokemon1)
        else:
            print(pokemon2.name+" attacks")
            pokemon2.inflict_damage(pokemon1)
            print(pokemon1.name+" attacks")
            pokemon1.inflict_damage(pokemon2)

    winner = pokemon1 if pokemon1.health > 0 else pokemon2
    print("The winner is " + winner.name)
    return winner

# bracket: list[Pokemon] -> list[Pokemon]
# starts battles tournament style between the pokemon of the list
# and returns a list that contains the winners of each battle


def bracket(tournament_list):
    new_list = []
    for i in range(0, len(tournament_list), 2):
        new_list += [battle(tournament_list[i], tournament_list[i+1])]
    return new_list

# begin_tournament: list[Pokemon] -> Pokemon
# takes a list of Pokemon that represents the contestants of a Tournament
# and returns the winner of the tournament


def begin_tournament(tournament_list):
    print("Let the matches begin!")
    while(len(tournament_list) > 1):
        print("Its time for the next round of battles")
        tournament_list = bracket(tournament_list)
    print("And the tournament winner is " + tournament_list[0].name)
    return tournament_list[0]

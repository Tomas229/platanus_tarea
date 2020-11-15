import Pokemon
import random


def makeTournament(n):
    participants = []
    for i in range(n):
        id = random.randrange(152)
        if(id == 0):
            id = 389  # Torterra
        participants += [Pokemon.Pokemon(id)]
    print("The contestants for this tournament are:")
    for i in participants:
        print(i.name)
    return participants


def beginTournament(tournament_list):
    print("Let the matches begin!")
    while(len(tournament_list) > 1):
        print("Its time for the next round of battles")
        tournament_list = bracket(tournament_list)
    print("And the tournament winner is " + tournament_list[0].name)
    return tournament_list


def bracket(tournament_list):
    new_list = []
    for i in range(0, len(tournament_list), 2):
        new_list += [battle(tournament_list[i], tournament_list[i+1])]
    return new_list


def battle(pokemon1, pokemon2):
    print(pokemon1.name + " vs " + pokemon2.name)
    winner = None
    while(pokemon1.health > 0 and pokemon2.health > 0):
        if(pokemon1.speed > pokemon2.speed):
            pokemon1.inflict_damage(pokemon2)
            pokemon2.inflict_damage(pokemon1)
        else:
            pokemon2.inflict_damage(pokemon1)
            pokemon1.inflict_damage(pokemon2)
    winner = pokemon1 if pokemon1.health > 0 else pokemon2
    print("The winner is " + winner.name)
    return winner


beginTournament(makeTournament(256))

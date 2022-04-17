import random
import sys

import pandas

import select_pokemon
from Player import Player

num_pokemon  = 3


if __name__ == '__main__':
    # num_pokemon = int(input("Enter number of Pokemon:"))
    num_pokemon = 3
    numPlayers = 2
    players = []
    for i in range(numPlayers):
        pokemonList = []
        for j in range(num_pokemon):
            pokemon = select_pokemon.select_random_pokemon_between(450,600)
            pokemon.select_random_attacks()
            pokemonList.append(pokemon)
        players.append(Player("Player 1", pokemonList))
        print(players[i])

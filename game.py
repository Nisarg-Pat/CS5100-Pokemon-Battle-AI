import random

import Data
from Controller.BattleController import BattleController
from Model.BattleModel import Model
from Model.Player import Player

num_pokemon = 3

if __name__ == '__main__':
    num_pokemon = 1
    numPlayers = 2
    players = []
    playerNames = ["Red", "Blue"]
    for i in range(numPlayers):
        pokemonList = []
        for j in range(num_pokemon):
            pokemon = Data.selectRandomPokemonBetween(450, 600)
            pokemonList.append(pokemon)
        players.append(Player(playerNames[i], pokemonList))
    model = Model(players)
    controller = BattleController(model)
    controller.start()

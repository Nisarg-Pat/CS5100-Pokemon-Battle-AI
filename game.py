import Data
from Controller.BattleController import BattleController
from Model.Model import Model
from Model.Player import Player

num_pokemon = 3

if __name__ == '__main__':
    num_pokemon = 3
    numPlayers = 2
    players = []
    for i in range(numPlayers):
        pokemonList = []
        for j in range(num_pokemon):
            pokemon = Data.selectRandomPokemonBetween(450, 600)
            pokemonList.append(pokemon)
        players.append(Player("Player 1", pokemonList))
    model = Model(players)
    controller = BattleController(model)
    controller.start()

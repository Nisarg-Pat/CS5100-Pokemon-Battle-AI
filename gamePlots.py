import random

import Data
import util
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player
import matplotlib.pyplot as plt

if __name__ == '__main__':
    numGames = 100
    x = [i + 1 for i in range(numGames)]
    y = [0 for i in range(numGames)]
    count = 0
    for i in range(numGames):
        print(i)
        numPokemon = 3
        agentTypes = [AgentEnum.MinimaxAgent, AgentEnum.RandomAgent]
        model = util.generateModel(numPokemon, agentTypes, False)
        BattleController(model).start()
        if model.winner == model.playerList[0]:
            count += 1
        y[i] = float(count) / float(x[i])
        # print(str(x[i])+" "+str(count)+" "+str(y[i]))
    plt.plot(x, y)
    plt.show()

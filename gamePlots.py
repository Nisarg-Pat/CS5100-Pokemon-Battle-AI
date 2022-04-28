import random

import Data
import util
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player
import matplotlib.pyplot as plt

if __name__ == '__main__':
    numGames = 5
    x = [i + 1 for i in range(numGames)]
    y = {"random": [0 for i in range(numGames)], "minimax": [0 for i in range(numGames)],
         "expectimax": [0 for i in range(numGames)], "qlearning": [0 for i in range(numGames)]}
    agents = {"random": AgentEnum.RandomAgent, "minimax": AgentEnum.MinimaxAgent,
         "expectimax": AgentEnum.Expectimax, "qlearning": AgentEnum.QLearningAgent}

    for q in y:
        count = 0
        for i in range(numGames):
            print(i)
            numPokemon = 3
            agentTypes = [AgentEnum.Expectimax(0), AgentEnum.RandomAgent(1)]
            model = util.generateModel(numPokemon, agentTypes, False)
            BattleController(model).start()
            if model.winner == model.playerList[0]:
                count += 1
            y[q][i] = float(count) / float(x[i])
        # print(str(x[i])+" "+str(count)+" "+str(y[i]))
        plt.plot(x, y[q])
    plt.show()

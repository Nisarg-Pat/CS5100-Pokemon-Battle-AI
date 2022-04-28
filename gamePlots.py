import random

import Data
import util
from AI import Agents, QLearning
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player
import matplotlib.pyplot as plt

if __name__ == '__main__':
    numGames = 10
    x = [i + 1 for i in range(numGames)]
    y = {"random": [0 for i in range(numGames)], "randomSuper": [0 for i in range(numGames)],
         "minimax": [0 for i in range(numGames)],
         "expectimax": [0 for i in range(numGames)], "qlearning": [0 for i in range(numGames)]}
    agents = {"random": Agents.RandomAgent(0), "minimax": Agents.MinimaxAgent(0),
              "randomSuper": Agents.RandomAgentAttackOnlySuperEffective(0),
         "expectimax": Agents.Expectimax(0), "qlearning": QLearning.ApproximateQAgent(0)}
    finalProb = {}
    legend = []
    for q in y:
        count = 0
        for i in range(numGames):
            print(i)
            numPokemon = 3
            agentTypes = [agents[q], Agents.RandomAgentAttackOnly(1)]
            model = util.generateModel(numPokemon, agentTypes, False)
            BattleController(model).start()
            if model.winner == model.playerList[0]:
                count += 1
            y[q][i] = float(count) / float(x[i])
        # print(str(x[i])+" "+str(count)+" "+str(y[i]))
        finalProb[q] = y[q][numGames-1]
        plt.plot(x, y[q])
        legend.append(q)
    plt.legend(legend)
    plt.xlabel("Number of games")
    plt.ylabel("Winning %")
    plt.title("Vs Random Agent")
    plt.show()
    print(finalProb)
import random

import Data
import util
from AI import Agents, QLearning, EvaluationFunctions
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player
import matplotlib.pyplot as plt

if __name__ == '__main__':
    numGames = 1000
    x = [i + 1 for i in range(numGames)]
    y = {"DamageDiff": [0 for i in range(numGames)], "OpponentDamageOnly": [0 for i in range(numGames)],
         "SelfDamageReduction": [0 for i in range(numGames)], "DamageDiffWithDefeats": [0 for i in range(numGames)]}
    agents = {"DamageDiff": Agents.Expectimax(0, EvaluationFunctions.DamageEvaluationFunction),
              "OpponentDamageOnly": Agents.Expectimax(0, EvaluationFunctions.OpponentDamageEvalFunc),
              "SelfDamageReduction": Agents.Expectimax(0, EvaluationFunctions.SelfDamageOnly),
              "DamageDiffWithDefeats": Agents.Expectimax(0, EvaluationFunctions.ComplexEval)}
    finalProb1 = {}
    legend = []
    finalProb2 = {}
    for q in y:
        count = 0
        for i in range(numGames):
            print(i)
            numPokemon = 3
            agentTypes = [agents[q], Agents.RandomAgent(1)]
            model = util.generateModel(numPokemon, agentTypes, False)
            BattleController(model).start()
            if model.winner == model.playerList[0]:
                count += 1
            y[q][i] = float(count) / float(x[i])
        # print(str(x[i])+" "+str(count)+" "+str(y[i]))
        finalProb2[q] = y[q][numGames-1]
        plt.plot(x, y[q])
        legend.append(q)
    plt.legend(legend)
    plt.xlabel("Number of games")
    plt.ylabel("Winning %")
    plt.title("Vs Agent Using Super Effective Moves")
    plt.show()

    print(finalProb1)
    print(finalProb2)
import random

import Data
import util
from AI import Agents, QLearning
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player


if __name__ == '__main__':
    numPokemon = 3
    agentTypes = [Agents.MinimaxAgent(0), Agents.RandomAgent(1)]
    model = util.generateModel(numPokemon, agentTypes, True)
    BattleController(model).start()

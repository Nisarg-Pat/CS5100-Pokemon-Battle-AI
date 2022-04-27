import random

import Data
import util
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player


if __name__ == '__main__':
    numPokemon = 3
    random.seed("Nisarg2")
    agentTypes = [AgentEnum.MinimaxAgent, AgentEnum.RandomAgent]
    model = util.generateModel(numPokemon, agentTypes, True)
    BattleController(model).start()

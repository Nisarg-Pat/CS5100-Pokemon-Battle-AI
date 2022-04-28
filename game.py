import random

import Data
import util
from AI import Agents
from Controller.BattleController import BattleController
from Model.AgentEnum import AgentEnum
from Model.BattleModel import Model
from Model.Player import Player


if __name__ == '__main__':
    numPokemon = 3
    random.seed("Nisarg4")
    agentTypes = [Agents.ManualAgent(0), Agents.RandomAgent(1)]
    model = util.generateModel(numPokemon, agentTypes, True)
    BattleController(model).start()

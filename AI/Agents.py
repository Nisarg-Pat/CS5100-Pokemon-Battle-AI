import random

import util
from Controller.Attack import Attack
from Controller.Switch import Switch
from Model.Action import Action


class Agent:

    def __init__(self, index=0):
        self.index = index


class RandomAgent(Agent):
    def getAction(self, model):
        actions = model.getLegalActions(self.index)
        # print(actions)
        choice = random.choice(actions)
        # print(choice)
        return choice


class ManualAgent(Agent):
    def getAction(self, model):
        if not model.requireSwitching():
            print("Your Current Pokemon: " + str(model.playerList[self.index].getCurrentPokemon()))
            print("Opponent's Current Pokemon: " +
                  str(model.playerList[model.getOpponentIndex(self.index)].getCurrentPokemon()))
            print()
            inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            inp = inp.lower()
            while inp not in util.selections:
                inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            if util.selections[inp] == 'A':
                return Attack(model, self.index).execute()
            elif util.selections[inp] == 'S':
                return Switch(model, self.index).execute()
            elif util.selections[inp] == 'Q':
                return (Action.QUIT, -1)

        else:
            if model.playerList[self.index].getCurrentPokemon().remainingHP == 0:
                return Switch(model, self.index).execute()
            else:
                return (Action.NONE, -1)

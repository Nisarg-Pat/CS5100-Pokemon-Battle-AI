import random

import util
from Controller.Attack import Attack
from Controller.Switch import Switch
from Model.Action import Action


class Agent:

    def __init__(self, index=0):
        self.index = index

    def getAction(self, model):
        return None

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

class RandomAgent(Agent):
    def getAction(self, model):
        actions = model.getLegalActions(self.index)
        choice = random.choice(actions)
        return choice

class MinimaxAgent(Agent):

    actionSequence = []

    def evaluationFunction(self, model):
        tot = 0.0
        for i in range(0, len(model.playerList)):
            if i == self.index:
                for pokemon in model.playerList[i].pokemonList:
                    tot -= 1 - (pokemon.hp - pokemon.remainingHP)/pokemon.hp
            else:
                for pokemon in model.playerList[i].pokemonList:
                    tot += 1 - (pokemon.hp - pokemon.remainingHP)/pokemon.hp
        # print(tot)
        print(self.actionSequence)
        return tot

    def getAction(self, model):
        legalActions = model.getLegalActions(self.index)
        maxScore = float("-inf")
        move = None
        for action in legalActions:
            self.actionSequence.append(action)
            # print(action)
            successorModel = model.generateSuccessor(self.index, action)
            # print(successorModel)
            score = self.minValue(successorModel, successorModel.getOpponentIndex(self.index), 0)
            if score > maxScore:
                maxScore = score
                move = action
            self.actionSequence.remove(action)
        print(maxScore)
        return move

    def minValue(self, model, agentIndex, depth):
        # print("In minValue")
        if model.isGameOver():
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        minScore = float("inf")
        for action in legalMoves:
            self.actionSequence.append(action)
            # print(action)
            successorModel = model.generateSuccessor(agentIndex, action)
            # print(successorModel)
            minScore = min(minScore, self.maxValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth + 1))
            self.actionSequence.remove(action)
        return minScore

    def maxValue(self, model, agentIndex, depth):
        # print("In MaxValue")
        if model.isGameOver() or depth == 1:
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        maxScore = float("-inf")
        for action in legalMoves:
            self.actionSequence.append(action)
            successorModel = model.generateSuccessor(agentIndex, action)
            maxScore = max(maxScore, self.minValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth))
            self.actionSequence.remove(action)
        return maxScore
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


class RandomAgentAttackOnly(Agent):
    def getAction(self, model):
        actions = model.getLegalActions(self.index)
        newActionList = []
        for action in actions:
            actionType, actionIndex = action
            if actionType == Action.ATTACK:
                newActionList.append(action)
        if len(newActionList) > 0:
            choice = random.choice(newActionList)
        else:
            choice = random.choice(actions)
        return choice


class MinimaxAgent(Agent):

    def evaluationFunction(self, model):
        tot1 = 0.0
        tot2 = 0.0
        for i in range(0, len(model.playerList)):
            if i == self.index:
                for pokemon in model.playerList[i].pokemonList:
                    tot1 += (pokemon.hp - pokemon.remainingHP)
            else:
                for pokemon in model.playerList[i].pokemonList:
                    tot2 += (pokemon.hp - pokemon.remainingHP)
        # print(tot)
        # print(str(self.actionSequence) +" "+str(tot1)+" "+str(tot2))
        return tot2 - tot1

    def getAction(self, model):
        legalActions = model.getLegalActions(self.index)
        maxScore = float("-inf")
        move = None
        for action in legalActions:
            # print(action)
            successorModel = model.generateSuccessor(self.index, action)
            # print(successorModel)
            score = self.minValue(successorModel, successorModel.getOpponentIndex(self.index), 0)
            print(score)
            if score > maxScore:
                maxScore = score
                move = action
        return move

    def minValue(self, model, agentIndex, depth):
        # print("In minValue")
        if model.isGameOver():
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        minScore = float("inf")
        for action in legalMoves:
            # print(action)
            successorModel = model.generateSuccessor(agentIndex, action)
            # print(successorModel)
            minScore = min(minScore,
                           self.maxValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth + 1))
        return minScore

    def maxValue(self, model, agentIndex, depth):
        # print("In MaxValue")
        if model.isGameOver() or depth == 2:
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        maxScore = float("-inf")
        for action in legalMoves:
            successorModel = model.generateSuccessor(agentIndex, action)
            maxScore = max(maxScore, self.minValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth))
        return maxScore


class Expectimax(Agent):

    def evaluationFunction(self, model):
        tot1 = 0.0
        tot2 = 0.0
        for i in range(0, len(model.playerList)):
            if i == self.index:
                for pokemon in model.playerList[i].pokemonList:
                    tot1 += (pokemon.hp - pokemon.remainingHP)
            else:
                for pokemon in model.playerList[i].pokemonList:
                    tot2 += (pokemon.hp - pokemon.remainingHP)
        # print(tot)
        # print(str(self.actionSequence) +" "+str(tot1)+" "+str(tot2))
        return tot2 - tot1

    def getAction(self, model):
        legalActions = model.getLegalActions(self.index)
        maxScore = float("-inf")
        move = None
        for action in legalActions:
            # print(action)
            successorModel = model.generateSuccessor(self.index, action)
            # print(successorModel)
            score = self.minValue(successorModel, successorModel.getOpponentIndex(self.index), 0)
            print(score)
            if score > maxScore:
                maxScore = score
                move = action
        return move

    def minValue(self, model, agentIndex, depth):
        # print("In minValue")
        if model.isGameOver():
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        avg = 0.0
        prob = 1.0 / (len(legalMoves))
        minScore = float("inf")
        for action in legalMoves:
            # print(action)
            successorModel = model.generateSuccessor(agentIndex, action)
            # print(successorModel)
            avg = avg + prob * self.maxValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth + 1)
        return minScore

    def maxValue(self, model, agentIndex, depth):
        # print("In MaxValue")
        if model.isGameOver() or depth == 2:
            return self.evaluationFunction(model)
        legalMoves = model.getLegalActions(agentIndex)
        maxScore = float("-inf")
        for action in legalMoves:
            successorModel = model.generateSuccessor(agentIndex, action)
            maxScore = max(maxScore, self.minValue(successorModel, successorModel.getOpponentIndex(agentIndex), depth))
        return maxScore

import random

import util
from AI.Agents import MinimaxAgent
from Model.Action import Action


class ApproximateQAgent:
    def __init__(self, index, discount=0.7, alpha=0.5, epsilon=0.3):
        self.index = index
        self.discount = discount
        self.alpha = alpha
        self.epsilon = epsilon
        self.features = {"PokemonHP", "PokemonRemainingHP", "OpponentHP", "OpponentRemainingHP", "Multiplier", "Damage",
                         "PokemonAttack", "PokemonDefense", "PokemonSpecialAttack", "PokemonSpecialDefense",
                         "PokemonSpeed", "OpponentAttack", "OpponentDefense", "OpponentSpecialAttack",
                         "OpponentSpecialDefense", "OpponentSpeed", "RemainingPokemon", "RemainingOpponent"}
        self.weights = {}
        for feature in self.features:
            self.weights[feature] = 0
        self.learn()

    def extractFeatures(self, model, action):
        features = {}
        copyModel = model.copy()
        currentPokemon = copyModel.playerList[self.index].getCurrentPokemon()
        opponentPokemon = copyModel.playerList[copyModel.getOpponentIndex(self.index)].getCurrentPokemon()
        actionType, actionIndex = action

        features["PokemonHP"] = currentPokemon.hp/1000
        features["PokemonRemainingHP"] = currentPokemon.remainingHP/1000
        features["OpponentHP"] = opponentPokemon.hp/1000
        features["OpponentRemainingHP"] = opponentPokemon.remainingHP/1000
        features["PokemonAttack"] = currentPokemon.attack/1000
        features["PokemonDefense"] = currentPokemon.defense/1000
        features["PokemonSpecialAttack"] = currentPokemon.special_attack/1000
        features["PokemonSpecialDefense"] = currentPokemon.special_defense/1000
        features["PokemonSpeed"] = currentPokemon.speed/1000
        features["OpponentAttack"] = opponentPokemon.attack/1000
        features["OpponentDefense"] = opponentPokemon.defense/1000
        features["OpponentSpecialAttack"] = opponentPokemon.special_attack/1000
        features["OpponentSpecialDefense"] = opponentPokemon.special_defense/1000
        features["OpponentSpeed"] = opponentPokemon.speed/1000
        features["RemainingPokemon"] = copyModel.playerList[self.index].getNumberOfPokemonLeft()/1000
        features["RemainingOpponent"] = copyModel.playerList[
            copyModel.getOpponentIndex(self.index)].getNumberOfPokemonLeft()/1000

        if actionType == Action.ATTACK:
            move = currentPokemon.moves[actionIndex - 1]
            multiplier, damage = currentPokemon.calcDamage(move, opponentPokemon)
            features["Multiplier"] = multiplier/1000
            features["Damage"] = damage/1000
        return features

    def calcReward(self, model):
        if model.winner is None:
            return 0
        elif model.winner == model.playerList[self.index]:
            return 100
        else:
            return -100
        # prevTot1 = 0.0
        # prevTot2 = 0.0
        # # # for pokemon in prevModel.playerList[self.index].pokemonList:
        # # #     prevTot1 += float(pokemon.hp - pokemon.remainingHP) / float(pokemon.hp)
        # for pokemon in prevModel.playerList[prevModel.getOpponentIndex(self.index)].pokemonList:
        #     prevTot2 += float(pokemon.hp - pokemon.remainingHP)
        # prevTot = (prevTot2 - prevTot1)
        # tot1 = 0.0
        # tot2 = 0.0
        # # # for pokemon in model.playerList[self.index].pokemonList:
        # # #     tot1 += float(pokemon.hp - pokemon.remainingHP) / float(pokemon.hp)
        # for pokemon in model.playerList[model.getOpponentIndex(self.index)].pokemonList:
        #     tot2 += float(pokemon.hp - pokemon.remainingHP)
        # tot = (tot2 - tot1)
        # return tot - prevTot

    def learn(self):
        numGames = 20
        # random.seed("Nisarg19")
        for i in range(numGames):
            print("Learning Game: " + str(i))
            numPokemon = 3
            from Model.AgentEnum import AgentEnum
            agentTypes = [AgentEnum.RandomAgent, AgentEnum.RandomAgent]
            model = util.generateModel(numPokemon, agentTypes, False)
            while not model.isGameOver():
                action = self.selectEpsilonGreedyAction(model)
                opponentIndex = model.getOpponentIndex(self.index)
                opponentAction = model.playerList[opponentIndex].agentType(opponentIndex).getAction(model)
                prevModel = model.copy()
                model.addAction(self.index, action)
                model.addAction(opponentIndex, opponentAction)

                reward = self.calcReward(model)
                self.update(prevModel, action, model, reward)
        print("Learning completed")

    def update(self, state, action, nextState, reward):
        difference = reward + (self.discount * self.computeValueFromQValues(nextState)) - self.getQValue(state, action)
        # print(difference)
        # print(self.computeValueFromQValues(nextState))
        # print(self.getQValue(state, action))
        featureList = self.extractFeatures(state, action)
        for feature in featureList:
            self.weights[feature] = self.weights[feature] + self.alpha * difference * featureList[feature]
        # print(self.weights)

    def selectEpsilonGreedyAction(self, model):
        legalActions = model.getLegalActions(self.index)
        r = random.random()
        if r < self.epsilon:
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(model)

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        QVal = 0.0
        featureList = self.extractFeatures(state, action)
        for feature in featureList:
            QVal = QVal + self.weights[feature] * featureList[feature]
        return QVal

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        legalActions = state.getLegalActions(self.index)
        if len(legalActions) == 0:
            return 0.0
        maxVal = float("-inf")
        for action in legalActions:
            maxVal = max(maxVal, self.getQValue(state, action))
        return maxVal

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        legalActions = state.getLegalActions(self.index)
        if len(legalActions) == 0:
            return None
        maxVal = float("-inf")
        maxActions = []
        for action in legalActions:
            if maxVal < self.getQValue(state, action):
                maxVal = self.getQValue(state, action)
                maxActions = [action]
            elif maxVal == self.getQValue(state, action):
                maxActions.append(action)
        choice = random.choice(maxActions)
        return choice

    def getAction(self, model):
        return self.computeActionFromQValues(model)

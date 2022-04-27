import util
from Model.Action import Action


class Player:

    def __init__(self, name, pokemonList, agent):
        self.name = name
        self.pokemonList = pokemonList
        self.currentPokemonIndex = 0
        self.agentType = agent

    def copy(self):
        newPokemonList = []
        for pokemon in self.pokemonList:
            newPokemonList.append(pokemon.copy())
        copyPlayer = Player(self.name, newPokemonList, self.agentType)
        copyPlayer.currentPokemonIndex = self.currentPokemonIndex
        copyPlayer.agentType = self.agentType
        return copyPlayer

    def getCurrentPokemon(self):
        return self.pokemonList[self.currentPokemonIndex]

    def getPokemonList(self):
        return self.pokemonList

    def getSwitchPokemonList(self):
        switchList = {}
        for i in range(len(self.pokemonList)):
            if self.pokemonList[i].remainingHP > 0 and self.pokemonList[i] != self.getCurrentPokemon():
                switchList[(i + 1)] = self.pokemonList[i]
        return switchList

    def getPossibleActions(self):
        actionList = []
        for action in self.getPossibleAttackActions():
            actionList.append(action)
        for action in self.getPossibleSwitchActions():
            actionList.append(action)
        return actionList

    def getPossibleSwitchActions(self):
        actionList = []
        for i in range(len(self.pokemonList)):
            if i != self.currentPokemonIndex and self.pokemonList[i].remainingHP > 0:
                actionList.append((Action.SWITCH, i + 1))
        return actionList

    def getPossibleAttackActions(self):
        actionList = []
        for i in range(len(self.getCurrentPokemon().getMoves())):
            actionList.append((Action.ATTACK, i + 1))
        return actionList

    def performAction(self, action, actionIndex, opponentPokemon, showPrints):
        actionIndex -= 1
        if action == Action.ATTACK:
            multiplier, damage = self.getCurrentPokemon().performMove(self.getCurrentPokemon().moves[actionIndex],
                                                                      opponentPokemon)
            if showPrints:
                print()
                print(self.getCurrentPokemon().name + " used " + self.getCurrentPokemon().moves[actionIndex].name)
                if multiplier != 1.0:
                    print(util.multiplierLine(multiplier))
                print(opponentPokemon.name + " took " + str(damage) + " damage. Remaining Health: " + str(
                    opponentPokemon.remainingHP) + "/" + str(opponentPokemon.hp))
                if opponentPokemon.remainingHP == 0:
                    print(opponentPokemon.name + " Fainted!!")

        elif action == Action.SWITCH:
            self.currentPokemonIndex = actionIndex
            if showPrints:
                print()
                print(self.name + " switched Pokemon to " + self.getCurrentPokemon().name)

    def getNumberOfPokemonLeft(self):
        count = 0
        for pokemon in self.pokemonList:
            if pokemon.remainingHP > 0:
                count += 1
        return count

    def __str__(self):
        string = ""
        for pokemon in self.pokemonList:
            string += str(pokemon) + "\n"
        return string

import util


class Player:

    def __init__(self, name, pokemonList):
        self.name = name
        self.pokemonList = pokemonList
        self.currentPokemonIndex = 0

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
        for move in self.getCurrentPokemon().getMoves():
            actionList.append(move)
        for i in range(len(self.pokemonList)):
            if i != self.currentPokemonIndex and self.pokemonList[i].remainingHP > 0:
                actionList.append("Pokemon " + str(i))
        print(actionList)

    def performAction(self, action, actionIndex, opponentPokemon):
        if action == "MOVE":
            multiplier, damage = self.getCurrentPokemon().performMove(self.getCurrentPokemon().moves[actionIndex],
                                                                      opponentPokemon)
            print()
            print(self.getCurrentPokemon().name + " used " + self.getCurrentPokemon().moves[actionIndex].name)
            if multiplier != 1.0:
                print(util.multiplierLine(multiplier))
            print(opponentPokemon.name + " took " + str(damage) + " damage. Remaining Health: " + str(
                opponentPokemon.remainingHP) + "/" + str(opponentPokemon.hp))
            if opponentPokemon.remainingHP == 0:
                print(opponentPokemon.name + " Fainted!!")

        elif action == "SWITCH":
            self.currentPokemonIndex = actionIndex - 1
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

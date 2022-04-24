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
        switchList = []
        for pokemon in self.pokemonList:
            if pokemon.remainingHP>0:
                switchList.append(pokemon)
        return switchList

    def getPossibleActions(self):
        actionList = []
        for move in self.getCurrentPokemon().getMoves():
            actionList.append(move)
        for i in range(len(self.pokemonList)):
            if i != self.currentPokemonIndex and self.pokemonList[i].remainingHP > 0:
                actionList.append("Pokemon " + str(i))
        print(actionList)

    def __str__(self):
        string = ""
        for pokemon in self.pokemonList:
            string += str(pokemon) + "\n"
        return string

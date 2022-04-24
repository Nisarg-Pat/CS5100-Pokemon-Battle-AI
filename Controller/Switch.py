class Switch:
    def __init__(self, model, agentIndex):
        self.model = model
        self.agentIndex = agentIndex

    def execute(self):
        switchList = self.model.playerList[0].getSwitchPokemonList()
        if len(switchList) == 0:
            print("No other pokemon left to switch.")
            return

        print("Pokemon List:")
        i = 1
        for pokemon in switchList:
            print(str(i) + "." + str(pokemon.name))
            i += 1
        inp = input("Select one of the Pokemon or type Back: ")

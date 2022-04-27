class Switch:
    def __init__(self, model, agentIndex):
        self.model = model
        self.agentIndex = agentIndex

    def execute(self):
        switchList = self.model.playerList[self.agentIndex].getSwitchPokemonList()
        if len(switchList) == 0:
            print("No other pokemon left to switch.")
            return

        print("Pokemon List:")
        selectionList = {}
        selectionList['back'] = -1
        for index in switchList:
            print(str(index) + "." + str(switchList[index].name))
            selectionList[str(index)] = index
            # lowerCaseMove = move.name.lower()
            selectionList[switchList[index].name.lower()] = index
        inp = input("Select one of the Pokemon or type Back: ")
        inp = inp.lower()
        while inp not in selectionList:
            inp = input("Please enter a valid move number or enter 'Back': ")
        if inp == "back":
            return
        pokemonIndex = selectionList[inp]
        self.model.addAction(self.agentIndex, "SWITCH", pokemonIndex)

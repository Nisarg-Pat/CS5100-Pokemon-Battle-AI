from Model.Action import Action


class Switch:
    def __init__(self, model, agentIndex):
        self.model = model
        self.agentIndex = agentIndex

    def execute(self):
        switchList = self.model.playerList[self.agentIndex].getSwitchPokemonList()
        if len(switchList) == 0:
            print("No other pokemon left to switch.")
            return None

        print("Pokemon List:")
        selectionList = {}
        if self.model.playerList[self.agentIndex].getCurrentPokemon().remainingHP > 0:
            selectionList['back'] = -1
        for index in switchList:
            print(str(index) + "." + str(switchList[index].name))
            selectionList[str(index)] = index
            selectionList[switchList[index].name.lower()] = index
        inp = input("Select one of the Pokemon: ")
        inp = inp.lower()
        while inp not in selectionList:
            inp = input("Please Select a Pokemon: ")
        if inp == "back":
            return None
        pokemonIndex = selectionList[inp]
        return (Action.SWITCH, pokemonIndex)


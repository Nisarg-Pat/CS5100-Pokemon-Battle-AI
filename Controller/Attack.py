class Attack:
    def __init__(self, model, agentIndex):
        self.model = model
        self.agentIndex = agentIndex

    def execute(self):
        print("Possible Moves:")
        i = 1
        attackList = self.model.playerList[self.agentIndex].getCurrentPokemon().moves
        selectionList = {}
        selectionList['back'] = -1
        for move in attackList:
            print(str(i) + "." + str(move.name))
            selectionList[str(i)] = i-1
            # lowerCaseMove = move.name.lower()
            selectionList[move.name.lower()] = i-1
            i += 1
        inp = input("Select one of possible moves or type Back: ")
        inp = inp.lower()
        while inp not in selectionList:
            inp = input("Please enter a valid move number or enter 'Back': ")
        if inp == "back":
            return
        moveIndex = selectionList[inp]
        self.model.addAction(self.agentIndex, "MOVE", moveIndex)

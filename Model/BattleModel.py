from Controller.Switch import Switch


class Model:

    def __init__(self, player):
        self.playerList = player
        self.gameOver = False
        self.turnNumber = 1
        self.turn = 0
        self.actionList = {}
        self.winner = None

    def isGameOver(self):
        return self.gameOver

    def addAction(self, playerIndex, action, actionIndex):
        self.actionList[playerIndex] = (action, actionIndex)
        self.turn = self.getOpponentIndex(self.turn)
        print(self.actionList)
        if len(self.actionList) == 2:
            self.performActions()

    def getOpponentIndex(self, playerIndex):
        return 1 - playerIndex

    def getCurrentPlayerIndex(self):
        return self.turn

    def performActions(self):
        if len(self.actionList) != 2:
            return
        currentPokemon = {}
        countMove = 0
        requireSwitchAction = {}
        for playerIndex in self.actionList:
            action, actionIndex = self.actionList[playerIndex]
            if action == "SWITCH":
                self.playerList[playerIndex].performAction(action, actionIndex, None)
                print("Player: " + str(playerIndex) + "Switched to : " + str(
                    self.playerList[playerIndex].getCurrentPokemon()))
            elif action == "MOVE":
                countMove += 1
            currentPokemon[playerIndex] = self.playerList[playerIndex].getCurrentPokemon()
        if countMove == 2:
            if currentPokemon[0].speed >= currentPokemon[1].speed:
                self.playerList[0].performAction(self.actionList[0][0], self.actionList[0][1], currentPokemon[1])
                if currentPokemon[1].remainingHP > 0:
                    self.playerList[1].performAction(self.actionList[1][0], self.actionList[1][1], currentPokemon[0])
                else:
                    requireSwitchAction[1] = True
            else:
                self.playerList[1].performAction(self.actionList[1][0], self.actionList[1][1], currentPokemon[0])
                if currentPokemon[0].remainingHP > 0:
                    self.playerList[0].performAction(self.actionList[0][0], self.actionList[0][1], currentPokemon[1])
                else:
                    requireSwitchAction[0] = True

        elif countMove == 1:
            for playerIndex in self.actionList:
                action, actionIndex = self.actionList[playerIndex]
                if action == "MOVE":
                    self.playerList[playerIndex].performAction(action, actionIndex,
                                                               currentPokemon[self.getOpponentIndex(playerIndex)])
                    if currentPokemon[self.getOpponentIndex(playerIndex)] == 0:
                        requireSwitchAction[self.getOpponentIndex(playerIndex)] = True

        self.actionList = {}

        if not requireSwitchAction:
            self.turnNumber += 1

        for playerIndex in requireSwitchAction:
            Switch(self, playerIndex).execute()
            self.addAction(self.getOpponentIndex(playerIndex), None, -1)

        if self.playerList[0].getNumberOfPokemonLeft() == 0:
            self.winner = self.playerList[1]
            self.gameOver = True
        elif self.playerList[1].getNumberOfPokemonLeft() == 0:
            self.winner = self.playerList[0]
            self.gameOver = True

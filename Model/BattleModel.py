from Controller.Switch import Switch
from Model.Action import Action


class Model:

    def __init__(self, player):
        self.playerList = player
        self.gameOver = False
        self.turnNumber = 1
        self.turn = 0
        self.actionList = {}
        self.winner = None
        self.loser = None

    def isGameOver(self):
        return self.gameOver

    def addAction(self, playerIndex, action):
        self.actionList[playerIndex] = action
        self.turn = self.getOpponentIndex(self.turn)
        if len(self.actionList) == 2:
            self.performActions()

    def getOpponentIndex(self, playerIndex):
        return 1 - playerIndex

    def getCurrentPlayerIndex(self):
        return self.turn

    def requireSwitching(self):
        if self.playerList[0].getCurrentPokemon().remainingHP == 0:
            return True
        if self.playerList[1].getCurrentPokemon().remainingHP == 0:
            return True

    def performActions(self):
        if len(self.actionList) != 2:
            return
        currentPokemon = {}
        countMove = 0
        requireSwitchAction = {}
        for playerIndex in self.actionList:
            (action, actionIndex) = self.actionList[playerIndex]
            if action == Action.SWITCH:
                self.playerList[playerIndex].performAction(action, actionIndex, None)
            elif action == Action.ATTACK:
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
                if action == Action.ATTACK:
                    self.playerList[playerIndex].performAction(action, actionIndex,
                                                               currentPokemon[self.getOpponentIndex(playerIndex)])
                    if currentPokemon[self.getOpponentIndex(playerIndex)] == 0:
                        requireSwitchAction[self.getOpponentIndex(playerIndex)] = True

        self.actionList = {}

        if not self.requireSwitching():
            self.turnNumber += 1

        if self.playerList[0].getNumberOfPokemonLeft() == 0:
            self.winner = self.playerList[1]
            self.loser = self.playerList[0]
            self.gameOver = True
        elif self.playerList[1].getNumberOfPokemonLeft() == 0:
            self.winner = self.playerList[0]
            self.loser = self.playerList[1]
            self.gameOver = True

    def getLegalActions(self, playerIndex):
        actions = []
        if self.requireSwitching():
            if self.playerList[playerIndex].getCurrentPokemon().remainingHP == 0:
                actions = self.playerList[playerIndex].getPossibleSwitchActions()
            else:
                actions = [(Action.NONE, -1)]
        else:
            actions = self.playerList[playerIndex].getPossibleActions()
        print(actions)
        return actions
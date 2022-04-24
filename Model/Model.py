class Model:

    def __init__(self, player):
        self.playerList = player
        self.gameOver = False
        self.turnNumber = 1

    def isGameOver(self):
        return self.gameOver

    def performAction(self, playerIndex, action, actionIndex):
        if action == "MOVE":
            playerPokemon = self.playerList[playerIndex].getCurrentPokemon()
            opponentPokemon = self.playerList[self.getOpponentIndex(playerIndex)].getCurrentPokemon()
            playerPokemon.performMove(playerPokemon.moves[actionIndex], opponentPokemon)

    def getOpponentIndex(self, playerIndex):
        return 1 - playerIndex

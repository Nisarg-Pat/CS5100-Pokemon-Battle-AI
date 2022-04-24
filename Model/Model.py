class Model:

    def __init__(self, player):
        self.playerList = player
        self.gameOver = False
        self.turnNumber = 1

    def isGameOver(self):
        return self.gameOver
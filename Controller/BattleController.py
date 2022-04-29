import util
from AI.Agents import ManualAgent, RandomAgent, MinimaxAgent
from Controller.Attack import Attack
from Controller.Switch import Switch
from Model.Action import Action
from Model.AgentEnum import AgentEnum


class BattleController:
    def __init__(self, model):
        self.model = model

    def start(self):
        if self.model.showPrints:
            print("Welcome to the Pokemon Battle")
            print("The following are the randomly selected Pokemon and their moves of you and Opponent:")
            print(self.model.playerList[0].name + "'s Team")
            print(self.model.playerList[0])
            print(self.model.playerList[1].name + "'s Team")
            print(self.model.playerList[1])
        counter = 0
        while not self.model.isGameOver():
            counter += 1
            playerIndex = self.model.getCurrentPlayerIndex()
            if self.model.showPrints:
                print("Turn " + str(self.model.turnNumber) + " Player: " + self.model.playerList[playerIndex].name)

            action = self.model.playerList[playerIndex].agentType.getAction(self.model)

            if action is not None:
                self.model.addAction(playerIndex, action)
            # print(self.model.actionList)
            if self.model.showPrints:
                print()

            if counter >= 1000:
                self.model.gameOver = True

        if self.model.isGameOver():
            if self.model.showPrints:
                if self.model.winner is not None:
                    print(self.model.loser.name + " is out of usable Pokemon.")
                    print(self.model.winner.name + " wins!!!")
                else:
                    print("Game Ended in a draw")

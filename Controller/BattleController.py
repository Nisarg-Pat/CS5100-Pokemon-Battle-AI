import util
from AI.Agents import ManualAgent, RandomAgent
from Controller.Attack import Attack
from Controller.Switch import Switch
from Model.Action import Action
from Model.AgentEnum import AgentEnum


class BattleController:
    def __init__(self, model):
        self.model = model

    def start(self):
        print("Welcome to the Pokemon Battle")
        print("The following are the randomly selected Pokemon and their moves of you and Opponent:")
        print(self.model.playerList[0].name+"'s Team")
        print(self.model.playerList[0])
        print(self.model.playerList[1].name+"'s Team")
        print(self.model.playerList[1])

        while not self.model.isGameOver():
            playerIndex = self.model.getCurrentPlayerIndex()
            print("Turn " + str(self.model.turnNumber) + " Player: " + self.model.playerList[playerIndex].name)

            if self.model.playerList[playerIndex].agentType == AgentEnum.ManualAgent:
                action = ManualAgent(playerIndex).getAction(self.model)
                if action is not None:
                    self.model.addAction(playerIndex, action)
            elif self.model.playerList[playerIndex].agentType == AgentEnum.RandomAgent:
                action = RandomAgent(playerIndex).getAction(self.model)
                if action is not None:
                    self.model.addAction(playerIndex, action)
            print(self.model.actionList)
            print()

        if self.model.isGameOver():
            print(self.model.loser.name+" is out of usable Pokemon.")
            print(self.model.winner.name+" wins!!!")

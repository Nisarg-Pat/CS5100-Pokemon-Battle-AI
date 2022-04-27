import util
from Controller.Attack import Attack
from Controller.Switch import Switch


class BattleController:
    def __init__(self, model):
        self.model = model

    def start(self):
        print("Welcome to the Pokemon Battle")
        print("The following are the randomly selected Pokemon and their moves of you and Opponent:")
        print("Your Pokemon")
        print(self.model.playerList[0])
        print("Opponent's Pokemon")
        print(self.model.playerList[1])

        while not self.model.isGameOver():
            playerIndex = self.model.getCurrentPlayerIndex()
            print("Turn " + str(self.model.turnNumber)+" Player: "+ str(playerIndex))
            print("Your Current Pokemon: " + str(self.model.playerList[playerIndex].getCurrentPokemon()))
            print("Opponent's Current Pokemon: " +
                  str(self.model.playerList[self.model.getOpponentIndex(playerIndex)].getCurrentPokemon()))
            print()

            inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            inp = inp.lower()
            while inp not in util.selections:
                inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            if util.selections[inp] == 'A':
                Attack(self.model, playerIndex).execute()
            elif util.selections[inp] == 'S':
                Switch(self.model, playerIndex).execute()
            elif util.selections[inp] == 'Q':
                return

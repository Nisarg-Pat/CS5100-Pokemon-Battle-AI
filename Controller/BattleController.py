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
            print("Turn " + str(self.model.turnNumber))
            print("Your Current Pokemon: " + str(self.model.playerList[0].getCurrentPokemon()))
            print("Opponent's Current Pokemon: " + str(self.model.playerList[1].getCurrentPokemon()))
            print()

            inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            inp = inp.lower()
            while inp not in util.selections:
                inp = input("Select one of the following: 1.Attack 2.Switch 3.Info: ")
            if (util.selections[inp] == 'A'):
                Attack(self.model, 0).execute()
            elif (util.selections[inp] == 'S'):
                Switch(self.model, 0).execute()
            self.model.gameOver = True
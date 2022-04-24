import random

import Data
import util


class Pokemon:
    def __init__(self, df):
        self.df = df
        self.name = df["Name"]
        self.type = df["Types"]
        self.hp = int(df["HP"])
        self.attack = int(df["Attack"])
        self.defense = int(df["Defense"])
        self.special_attack = int(df["Special Attack"])
        self.special_defense = int(df["Special Defense"])
        self.speed = int(df["Speed"])

        self.moves = []
        self.allMovesList = []
        moves = util.move_to_list(df["Moves"])
        for move in moves:
            self.allMovesList.append(Data.getMove(move))

        self.remainingHP = self.hp

    def getMoves(self):
        return self.moves

    def __str__(self):
        return self.name + ": " + str(self.remainingHP) + "/" + str(self.hp) + " "+ str(self.moves)

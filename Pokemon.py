import random

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

        self.moves = {}

        self.remainingHP = self.hp


    def select_random_attacks(self):
        # print(util.str_to_list(self.df["Moves"]))
        move_list = util.move_to_list(self.df["Moves"])
        self.moves = random.sample(move_list, min(4, len(move_list)))

    def getMoves(self):
        return self.moves

    def __str__(self):
        return self.name + ": " + str(self.remainingHP) + "/" + str(self.hp) + " "+ str(self.moves)

import random

import Data
import util


class Pokemon:
    def __init__(self, df):
        self.df = df
        self.name = df["Name"]
        self.type = util.type_to_list(df["Types"])
        self.hp = (2*int(df["HP"])+31)+110
        self.attack = (2*int(df["Attack"])+31)+5
        self.defense = (2*int(df["Defense"])+31)+5
        self.special_attack = (2*int(df["Special Attack"])+31)+5
        self.special_defense = (2*int(df["Special Defense"])+31)+5
        self.speed = (2*int(df["Speed"])+31)+5

        self.moves = []
        self.allMovesList = []
        moves = util.move_to_list(df["Moves"])
        for move in moves:
            self.allMovesList.append(Data.getMove(move))

        self.remainingHP = self.hp

    def getMoves(self):
        return self.moves

    def performMove(self, move, opponent):
        multiplier = util.getMultiplier(move.type, opponent.type)
        if move.category == "Physical":
            ad = float(self.attack) / float(opponent.defense)
        else:
            ad = float(self.special_attack) / float(opponent.special_defense)
        stab = 1.0
        if move.type in self.type:
            stab = 1.5
        maxDamage = int((0.85*float(move.power)*ad)*multiplier*stab)
        minDamage = int(0.85*maxDamage)
        print(str(maxDamage)+" "+str(minDamage))
        opponent.damage(maxDamage)

    def damage(self, val):
        self.remainingHP = max(self.remainingHP-val, 0)

    def __str__(self):
        return self.name + ": " + str(self.remainingHP) + "/" + str(self.hp) + " "+ str(self.moves)

import pandas

import Data
from Model.BattleModel import Model
from Model.Player import Player

selections = {"1": "A", "a": "A", "attack": "A", "2": "S", "s": "S", "switch": "S", "3": "I", "i": "I", "info": "I",
              "quit": "Q"}

type_chart = pandas.read_csv("Data/Type_Chart.csv", sep=',')
type_chart_dict = {}
types = list(type_chart.columns)
types.remove("Attacking")
for index, row in type_chart.iterrows():
    type_chart_dict[row["Attacking"]] = {}
    for column in types:
        type_chart_dict[row["Attacking"]][column] = float(row[column])


def move_to_list(s):
    s = s.replace("[", "").replace("]", "")
    s = s.split(", ")
    for i in range(len(s)):
        s[i] = s[i][1:-1]
        s[i] = reformat(s[i])
    return s


def type_to_list(s):
    return move_to_list(s)


def reformat(s):
    return s


def getMultiplier(attackType, defenseTypes):
    multiplier = 1.0
    # print(type_chart)
    for defenseType in defenseTypes:
        multiplier *= type_chart_dict[attackType][defenseType]
    # print(df)
    return multiplier


def multiplierLine(multiplier):
    if multiplier == 0.0:
        return "It Does Not Affect."
    elif multiplier < 1.0:
        return "It's Not Very Effective."
    elif multiplier > 1.0:
        return "It's Super Effective"
    else:
        return ""


def generateModel(numPokemon, agentTypes, showPrints):
    numPlayers = 2
    players = []
    playerNames = ["Red", "Blue"]

    for i in range(numPlayers):
        pokemonList = []
        for j in range(numPokemon):
            pokemon = Data.selectRandomPokemonBetween(450, 600)
            pokemonList.append(pokemon)
        players.append(Player(playerNames[i], pokemonList, agentTypes[i]))
    return Model(players, showPrints)

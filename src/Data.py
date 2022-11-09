import random

import pandas

import util
from Model.Move import Move
from Model.Pokemon import Pokemon


def readPokemonList():
    pokemon_list = pandas.read_csv("Data/Pokemon_Data.csv", sep=';')
    pokemon_list["Total"] = pokemon_list.HP + pokemon_list.Attack + pokemon_list.Defense + pokemon_list[
        "Special Attack"] + pokemon_list["Special Defense"] + pokemon_list.Speed
    pokemon_list = pokemon_list[pokemon_list["Total"] >= 450]
    pokemon_list = pokemon_list[pokemon_list["Total"] <= 600]
    pokemon_list_dict = {}
    columns = list(pokemon_list.columns)
    for index, row in pokemon_list.iterrows():
        pokemon_list_dict[row["Name"]] = {}
        for column in columns:
            pokemon_list_dict[row["Name"]][column] = row[column]
    return pokemon_list_dict


def readMoveList():
    move_list = pandas.read_csv("Data/Move.csv")
    for i in range(0, len(move_list)):
        s = move_list.loc[i, "Name"]
        move_list.loc[i, "Name"] = util.reformat(s)
    move_list_dict = {}
    columns = list(move_list.columns)
    for index, row in move_list.iterrows():
        move_list_dict[row["Name"]] = {}
        for column in columns:
            move_list_dict[row["Name"]][column] = row[column]
    return move_list_dict


moves_list = readMoveList()
pokemon_list = readPokemonList()


def selectRandomPokemonBetween(low, high):
    df = random.choice(list(pokemon_list))
    pokemon = Pokemon(pokemon_list[df])
    selectRandomAttackingMoves(pokemon)
    return pokemon


def selectRandomMoves(pokemon):
    pokemon.moves = random.sample(pokemon.allMovesList, 4)


def selectRandomAttackingMoves(pokemon):
    possibleMoves = []
    for move in pokemon.allMovesList:
        if move.power!="None":
            possibleMoves.append(move)
    pokemon.moves = random.sample(possibleMoves, 4)

def getMove(move):
    df = moves_list[move]
    newMove = Move(df)
    return newMove

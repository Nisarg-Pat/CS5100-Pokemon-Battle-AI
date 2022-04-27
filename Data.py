import random

import pandas

import util
from Model.Move import Move
from Model.Pokemon import Pokemon


def readPokemonList():
    pokemon_list = pandas.read_csv("Data/Pokemon_Data.csv", sep=';')
    pokemon_list["Total"] = pokemon_list.HP + pokemon_list.Attack + pokemon_list.Defense + pokemon_list[
        "Special Attack"] + pokemon_list["Special Defense"] + pokemon_list.Speed
    return pokemon_list


def readMoveList():
    move_list = pandas.read_csv("Data/Move.csv")
    for i in range(0, len(move_list)):
        s = move_list.loc[i, "Name"]
        move_list.loc[i, "Name"] = util.reformat(s)
    return move_list


moves_list = readMoveList()
pokemon_list = readPokemonList()


def selectRandomPokemon():
    df = pokemon_list.iloc[random.randint(0, len(pokemon_list))]
    print(df)
    return Pokemon(df)


def selectRandomPokemonBetween(low, high):
    pokemonList = pokemon_list
    pokemonList = pokemonList[pokemonList["Total"] >= low]
    pokemonList = pokemonList[pokemonList["Total"] <= high]
    df = pokemonList.iloc[random.randint(0, len(pokemonList) - 1)]
    pokemon = Pokemon(df.to_dict())
    selectRandomAttackingMoves(pokemon)
    return pokemon


def selectAllPokemon():
    pokemonList = pokemon_list
    pokemonList = pokemonList[pokemonList["Total"] >= 450]
    pokemonList = pokemonList[pokemonList["Total"] <= 600]
    for i in range(0, len(pokemonList)):
        pokemon = Pokemon(pokemonList.iloc[i])
        moves = util.move_to_list(pokemon.df["Moves"])
        for i in range(0, len(moves)):
            if moves[i] != pokemon.allMovesList[i].name:
                return
        selectRandomAttackingMoves(pokemon)
    print("Completed")


def selectRandomMoves(pokemon):
    pokemon.moves = random.sample(pokemon.allMovesList, 4)


def selectRandomAttackingMoves(pokemon):
    possibleMoves = []
    for move in pokemon.allMovesList:
        if move.power!="None":
            possibleMoves.append(move)
    # pokemon.moves = random.sample(possibleMoves, min(4, len(possibleMoves)))
    pokemon.moves = random.sample(possibleMoves, 4)

def getMove(move):
    df = moves_list[moves_list["Name"] == move].iloc[0]
    newMove = Move(df)
    return newMove

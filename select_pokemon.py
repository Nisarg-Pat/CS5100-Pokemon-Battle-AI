import random

import pandas

from Pokemon import Pokemon


def read_pokemon_list():
    pokemon_list = pandas.read_csv("Data/Pokemon_Data.csv", sep=';')
    pokemon_list["Total"] = pokemon_list.HP + pokemon_list.Attack + pokemon_list.Defense + pokemon_list[
        "Special Attack"] + pokemon_list["Special Defense"] + pokemon_list.Speed
    return pokemon_list

def select_random_pokemon():
    pokemon_list = read_pokemon_list()
    df = pokemon_list.iloc[random.randint(0, len(pokemon_list))]
    print(df)
    return Pokemon(df)

def select_random_pokemon_between(low, high):
    pokemon_list = read_pokemon_list()
    pokemon_list = pokemon_list[pokemon_list["Total"] >= low]
    pokemon_list = pokemon_list[pokemon_list["Total"] <= high]
    df = pokemon_list.iloc[random.randint(0, len(pokemon_list))]
    return Pokemon(df)
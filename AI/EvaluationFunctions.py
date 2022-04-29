class DamageEvaluationFunction:
    def evaluate(self, model, index):
        tot1 = 0.0
        tot2 = 0.0
        for pokemon in model.playerList[index].pokemonList:
            tot1 += (pokemon.hp - pokemon.remainingHP)
        for pokemon in model.playerList[model.getOpponentIndex(index)].pokemonList:
            tot2 += (pokemon.hp - pokemon.remainingHP)
        return tot2 - tot1

class OpponentDamageEvalFunc:
    def evaluate(self, model, index):
        tot1 = 0.0
        tot2 = 0.0
        for pokemon in model.playerList[model.getOpponentIndex(index)].pokemonList:
            tot2 += (pokemon.hp - pokemon.remainingHP)
        return tot2 - tot1

class SelfDamageOnly:
    def evaluate(self, model, index):
        tot1 = 0.0
        tot2 = 0.0
        for pokemon in model.playerList[index].pokemonList:
            tot1 += (pokemon.hp - pokemon.remainingHP)
        return tot2 - tot1

class ComplexEval:
    def evaluate(self, model, index):
        tot1 = 0.0
        tot2 = 0.0
        numPokemon = 0
        for pokemon in model.playerList[index].pokemonList:
            tot1 += (pokemon.hp - pokemon.remainingHP)
            numPokemon+=1
        tot1+=(1000)*(numPokemon - model.playerList[index].getNumberOfPokemonLeft())

        for pokemon in model.playerList[model.getOpponentIndex(index)].pokemonList:
            tot2 += (pokemon.hp - pokemon.remainingHP)

        tot2+=(1000)*(numPokemon - model.playerList[model.getOpponentIndex(index)].getNumberOfPokemonLeft())
        return tot2 - tot1
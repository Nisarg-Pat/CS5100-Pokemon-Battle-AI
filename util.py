import pandas

selections = {"1": "A", "a": "A", "attack": "A", "2": "S", "s": "S", "switch": "S", "3": "I", "i": "I", "info": "I",
              "quit": "Q"}


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
    type_chart = pandas.read_csv("Data/Type_Chart.csv", sep=',')
    # print(type_chart)
    df = type_chart[type_chart["Attacking"] == attackType]
    for defenseType in defenseTypes:
        # print(df[defenseType])
        multiplier = multiplier * float(df[defenseType])
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

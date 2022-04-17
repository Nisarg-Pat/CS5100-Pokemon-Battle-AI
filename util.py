import pandas


def move_to_list(s):
    s = s.replace("[", "").replace("]", "")
    s = s.split(", ")
    for i in range(len(s)):
        s[i] = s[i][1:-1]
        s[i] = s[i].replace("'", " ")
    return s


def getMultiplier(attackType, defenseTypes):
    multiplier = 1.0
    type_chart = pandas.read_csv("Data/Type_Chart.csv", sep=',')
    print(type_chart)
    df = type_chart[type_chart["Attacking"] == attackType]
    for defenseType in defenseTypes:
        print(df[defenseType])
        multiplier = multiplier * float(df[defenseType])
    # print(df)
    return multiplier

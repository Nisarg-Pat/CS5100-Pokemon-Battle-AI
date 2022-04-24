class Move:
    def __init__(self, df):
        self.df = df
        self.name = str(df["Name"])
        self.type = str(df["Type"])
        self.category = str(df["Category"])
        self.power = str(df["Power"])
        self.accuracy = str(df["Accuracy"])

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

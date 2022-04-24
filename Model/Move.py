class Move:
    def __init__(self, df):
        self.df = df
        self.name = df["Name"]
        self.type = df["Type"]
        self.category = df["Category"]
        self.power = df["Power"]
        self.accuracy = df["Accuracy"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

class Player:
    def __init__(self,name, id_code , ppg, apg, rpg, spg, bpg, mpg, fg_perc, three_pt_perc):
        name = name
        self.id_code = id_code
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.spg = spg
        self.bpg = bpg
        self.mpg = mpg
        self.fg_perc = fg_perc
        self.three_pt_perc = three_pt_perc

    def display_stats(self):
        print(self.name)
        print("----------------------")
        print(f"Points per game: {self.ppg}")
        print(f"Rebounds per game: {self.rpg}")
        print(f"Assists per game: {self.apg}")
        print(f"Steals per game: {self.spg}")
        print(f"Blocks per game: {self.bpg}")
        print(f"Minutes per game: {self.mpg}")
        print(f"Field Goal Percentage: {round(self.fg_perc * 100, 1)}%")
        print(f"Three Point Percentage: {round(self.three_pt_perc * 100, 1)}%")




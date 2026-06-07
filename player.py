class Player:
    def __init__(self,name, id_code , ppg, apg, rpg, spg, bpg, mpg, fg_perc, three_pt_perc, season):
        self.name = name
        self.id_code = id_code
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg
        self.mpg = mpg
        self.fg_perc = fg_perc
        self.three_pt_perc = three_pt_perc
        self.season = season

    def display_stats(self):
        print(f"\nSeason: {self.season}")
        print(self.name)
        print("----------------------")
        print(f"Points per game: {round(self.ppg, 1)}")
        print(f"Assists per game: {round(self.apg, 1)}")
        print(f"Rebounds per game: {round(self.rpg, 1)}")
        print(f"Steals per game: {round(self.spg, 1)}")
        print(f"Blocks per game: {round(self.bpg, 1)}")
        print(f"Minutes per game: {round(self.mpg, 1)}")
        print(f"Field Goal Percentage: {round(self.fg_perc * 100, 1)}%")
        print(f"Three Point Percentage: {round(self.three_pt_perc * 100, 1)}%")




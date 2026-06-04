class Player:
    def __init__(self,name, id_code , ppg, apg, rpg, spg, bpg, mpg, fg_perc, three_pt_perc):
        name = name
        self.id_code = id_code
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg
        self.mpg = mpg
        self.fg_perc = fg_perc
        self.three_pt_perc = three_pt_perc

    def display_stats(self):
        print(self.name)
        print("\n----------------------")
        



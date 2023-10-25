class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing cricket")
class Batsman(Player):
    def play(self):
        print(f"{self.name} is batting")
class Bowler(Player):
    def play(self):
        print(f"{self.name} is bowling")
batsman = Batsman("Rakesh")
bowler = Bowler("Dinesh")
batsman.play()
bowler.play()
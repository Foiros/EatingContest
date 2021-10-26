
class Food:
    def __init__(self, name: str, scoreValue: int, timeLost: int, smells: bool):
        self.name = name
        self.scoreValue = scoreValue
        self.timeLost = timeLost
        self.smells = smells

    def getScoreValue(self):
        return self.scoreValue

    def get_time_lost(self):
        return self.timeLost

import random

class DiceService:
    def __init__(self, dice, num_dice):
        self.dice = dice
        self.num_dice = num_dice

    def roll(self):
        return random.randint(1, self.num_dice * self.dice.get_size())

    def get_num_dice(self):
        return self.num_dice
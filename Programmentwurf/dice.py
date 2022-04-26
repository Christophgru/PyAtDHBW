"""
dice-class file
"""
import random
from datetime import datetime


class Dice:
    """
    dice-class, that contains the value of generated dices
    """
    def __init__(self):
        self.eyes = None
        self.isactivated = False
        random.seed(datetime.now().microsecond)

    def throw(self) -> int:
        self.eyes = random.randint(1, 6)
        return self.eyes

    def deactivate(self):
        """setzte activated auf F und eyes auf -1 oder so
        """
        self.isactivated = False


    def activate(self):
        """setzte activated auf T"""
        self.isactivated = True

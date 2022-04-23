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
        self.augen = None
        self.isactivated = False
        random.seed(datetime.now())

    def throw(self) -> int:
        """todo:ali set self. augen auf random wert"""
        self.augen = random.randint(1, 6)
        return self.augen

    def deactivate(self):
        """setzte activated auf F und augen auf -1 oder so
        """
        self.isactivated = False


    def activate(self):
        """setzte activated auf T"""
        self.isactivated = True

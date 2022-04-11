# ali
import random



class Dice:
    def __init__(self):
        self.augen = None
        self.isactivated = False

    def throw(self) -> int:
        """todo:ali set self. augen auf random wert"""
        self.augen = random.randint(1, 6)
        return self.augen

    def deactivate(self):
        """setzte activated auf F und augen auf -1 oder so
        """
        self.isactivated = False

        self.augen = None

    def activate(self):
        """setzte activated auf T"""
        self.isactivated = True

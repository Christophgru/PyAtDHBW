# ali
import self as self


class Dice:
    def __init__(self):
        self.augen: int = -1
        self.isactivated = False

    def throw(self) -> int:
        """todo:ali set self. augen auf random wert"""
        self.augen = 3
        return self.augen

    def deactivate(self):
        """setzte activated auf F und augen auf -1 oder so
        """
        self.isactivated = False
        self.augen = -1

    def activate(self):
        """setzte activated auf T"""
        self.isactivated = True

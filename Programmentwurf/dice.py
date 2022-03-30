# ali
import self as self


class Dice:
    def __init__(self):
        self.augen: int = -1
        self.isactivated = False


    def throw(self) -> int:
        """todo:set self. aufgen auf random wert
        """

    def deactivate(self):
        """setzte activated auf F und augen auf -1 oder so
        """
        self.isactivated = False
        self.augen=-1

    def activate(self):
        """setzte activated auf T"""
        self.isactivated = True

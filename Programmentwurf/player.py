"""
@todo pve in player class, dann ist der letzte pylint fehler weg (man braucht min 2 public methoden)
player-class-file
"""


class Player:
    """
    player-class
    """
    def __init__(self, istecht: bool, name: str):
        self.istecht: bool = istecht
        self.name: str = name

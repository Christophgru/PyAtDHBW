"""
@todo pve in player class, dann ist der letzte pylint fehler weg (man braucht min 2 public methoden)
player-class-file
"""
from io import StringIO
from unittest.mock import patch


class Player:
    """
    player-class
    """

    def __init__(self, istecht: bool, name: str):
        self.istecht: bool = istecht
        self.name: str = name

    def choosediceorcheck(self, dicedict, ui, player1, activeplayer):
        if activeplayer == 2 and not self.istecht:
            inputstring = "1\n1\n1\n"
            with patch('sys.stdout', new=StringIO()) as fake_out:
                with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                    ui.choosediceorcheck(dicedict)
        else:
            ui.choosediceorcheck(dicedict)

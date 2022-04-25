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

    def choosediceorcheck(self, dicedict, ui, activeplayer):
        if activeplayer == 1 and not self.istecht:
            inputstring = "1\n"
            with patch('sys.stdout', new=StringIO()) as fake_out:
                with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                    ui.choosediceorcheck(dicedict)
        else:
            ui.choosediceorcheck(dicedict)

    def choose_action_with_dice_arr(self, ui,
                                    dicedict,
                                    spielblock,
                                    activeplayer,
                                    p1name, iter):
        namearr = [p1name, self.name]
        if activeplayer == 1 and not self.istecht:
            options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
            wahl = options[iter]
            inputstring: str = str(wahl) + "\n"
            with patch('sys.stdout', new=StringIO()) as fake_out:
                with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                    if "Sind Sie Sicher?" in fake_out.read(20):
                        fake_in.write("0\n")
                    return ui.choose_action_with_dice_arr(dicedict, spielblock, activeplayer, namearr)
        else:
            return ui.choose_action_with_dice_arr(dicedict, spielblock, activeplayer, namearr)

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

    def choosediceorcheck(self, dicedict, _ui, activeplayer):
        """

        @param dicedict:
        @type dicedict:
        @param _ui:
        @type _ui:
        @param activeplayer:
        @type activeplayer:
        @return:
        @rtype:
        """
        if activeplayer == 1 and not self.istecht:
            inputstring = "1\n"
            with patch('sys.stdout', new=StringIO()):
                with patch('sys.stdin', new=StringIO(inputstring)):
                    _ui.choosediceorcheck(dicedict)
        else:
            _ui.choosediceorcheck(dicedict)

    def choose_action_with_dice_arr(self, _ui,
                                    dicedict,
                                    spielblock,
                                    activeplayer,
                                    p1name,
                                    spielzug):
        """

        @param _ui:
        @type _ui:
        @param dicedict:
        @type dicedict:
        @param spielblock:
        @type spielblock:
        @param activeplayer:
        @type activeplayer:
        @param p1name:
        @type p1name:
        @param spielzug:
        @type spielzug:
        @return:
        @rtype:
        """
        if activeplayer == 1 and not self.istecht:
            options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
            wahl = options[spielzug - 1]
            inputstring: str = str(wahl) + "\n"
            with patch('sys.stdout', new=StringIO()) as fake_out:
                with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                    if "geben sie etwas anders ein" in fake_out.read(20):
                        fake_in.write("0\n")

                    result = _ui.choose_action_with_dice_arr(dicedict, spielblock, activeplayer, [p1name, self.name])
                    return result
        else:
            return _ui.choose_action_with_dice_arr(dicedict, spielblock, activeplayer, [p1name, self.name])

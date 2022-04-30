"""
test-file
"""
from unittest.mock import patch

import game as Game
import gameblock as Block
from io import StringIO
from unittest import TestCase


class TestKniffel(TestCase):
    """
    todo: all: testet was das zeug hält
    """

    def testGameblock(self):
        block: Block = Block.Gameblock()
        block.freeze(block)
        thawed = block.thaw()

        self.assertEqual(type(thawed), type(block))
        self.assertEqual(block.gamened(), False)

    def testblockAusgabe(self):
        block: Block = Block.Gameblock()
        block.output("Steve", "Steve's Opfer'")

    def testPVP(self):
        # buildString
        inputstring = "1\n"  # choose gamemode: pvp
        inputstring += "Ulli\nDulli\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]  # zeileneingabe vorbereitung
        for i in range(0, 13):
            inputstring += "1,2\n3,4\n"  # waehle keine wuerfel
            inputstring += str(options[i]) + "\n"  # dann zeile für eintrag aus Options
            if options[i] >= 10:  # zeile nicht erfüllbar nur bei >10
                inputstring += "0\n0\n0\n"  # falls Zeile nicht erfüllbar trage 0 ein

            inputstring += "0\n0\n" + str(options[i]) + "\n"  # das selbe für den anderen mitgameer
            if options[i] >= 10:
                inputstring += "0\n0\n0\n"
        # insert String, check ob durchgelaufen ist
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fakein:
                game = Game.Game()
                game.startgame()
                strout: str = fake_out.getvalue()
                self.assertTrue("Game Vorbei" in strout)
        print(strout)

    def testinvalidGameblock(self):
        spiel: Game = Game.Game()
        block: Block = spiel.gameblock
        block.inputpoints(1, 0, False, 1, 1, 2, 3, 1)

    def testPVE(self):
        """
    ein test dieser Methodik funktioniert bei PvE nicht,
    da der TEst und der E-Player den delben eingabestrem nutzen
        @return:
        """
        inputstring = "2\nspieler1\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
        for i in range(0, 13):
            inputstring += "1,2,3\n4\n" + str(options[i]) + "\n"
            if options[i] >= 10:
                inputstring += "0\n0\n0\n"
        with patch('sys.stdout', new=StringIO()) as fakeout:
            with patch('sys.stdin', new=StringIO(inputstring)):
                game = Game.Game()
                game.startgame()
                ausgabe = fakeout.getvalue()
                self.assertTrue("Der Gewinner ist" in ausgabe)

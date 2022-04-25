import unittest
from unittest.mock import patch

import spiel as Spiel
import spielblock as Block
from io import StringIO
from unittest import TestCase


class TestKniffel(TestCase):
    """
    todo: all: testet was das zeug hält
    """


    def testSpielblock(self):
        block: Block = Block.Spielblock()
        block.freeze(block)
        thawed = block.thaw()

        self.assertEqual(type(thawed), type(block))
        self.assertEqual(block.gamened(), False)

    def testblockAusgabe(self):
        block: Block = Block.Spielblock()
        block.ausgabe("Steve", "Steve's Opfer'")


    def testPVP(self):
        # buildString
        inputstring = "1\n"  # choose gamemode: pvp
        inputstring += "player1\nplayer2\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]  # zeileneingabe vorbereitung
        for i in range(0, 13):
            inputstring += "0\n0\n" + str(options[i]) + "\n"  # waehle keine wuerfel, dann zeile für eintrag aus Options
            if options[i] >= 10:  # zeile nicht erfüllbar nur bei >10
                inputstring += "0\n0\n0\n"  # falls Zeile nicht erfüllbar trage 0 ein

            inputstring += "0\n0\n" + str(options[i]) + "\n"  # das selbe für den anderen mitspieler
            if options[i] >= 10:
                inputstring += "0\n0\n0\n"
        # insert String, check ob durchgelaufen ist
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fakein:
                spiel = Spiel.Spiel()
                spiel.spielstarten()
                strout: str = fake_out.getvalue()
                self.assertTrue("Spiel Vorbei" in strout)


    def testinvalidSpielblock(self):
        block: Block = Block.Spielblock()
        block.punkteeinlesen(1, 0, False, 1, 1, 2, 3, 1)

    def testPVE(self):
        """
    ein test dieser Methodik funktioniert bei PvE nicht,
    da der TEst und der E-Player den delben eingabestrem nutzen
        @return:
        """
        inputstring = "2\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
        for i in range(0, 13):
            inputstring += "0\n0\n" + str(options[i]) + "\n"
            if options[i] >= 10:
                inputstring += "0\n0\n0\n"
        with patch('sys.stdout', new=StringIO()) as fakeout:
            with patch('sys.stdin', new=StringIO(inputstring)) as fakein:
                spiel = Spiel.Spiel()
                spiel.spielstarten()
                self.assertTrue("Der Gewinner ist" in fakeout.read(100))


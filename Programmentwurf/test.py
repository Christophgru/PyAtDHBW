
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

    def testSpielStarten(self):
        spiel = Spiel.Spiel()
        self.assertTrue(spiel.spielstarten())

    def testSpielblock(self):
        block: Block = Block.Spielblock()
        block.freeze(block)
        thawed = block.thaw()

        self.assertEqual(type(thawed), type(block))
        self.assertEqual(block.gamened(), False)

    def testblockAusgabe(self):
        block: Block = Block.Spielblock()
        block.ausgabe("Steve", "Steve's Opfer'")

    def testinvalidSpielblock(self):
        block: Block = Block.Spielblock()
        block.punkteeinlesen(1, 0, False, 1, 1, 2, 3, 1)

    def testPVE(self):
        inputstring = "2\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
        for i in range(1, 13):
            inputstring += "1\n1\n1\n" + str(options[i]) + "\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                spiel = Spiel.Spiel()
                spiel.spielstarten()




from unittest.mock import patch

import spiel as Spiel
import spielblock as Block
from io import StringIO
from unittest import TestCase


class TestSnackautomat3(TestCase):
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

    def testPVE(self):
        inputstring = "2\n"
        options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
        for i in range(1, 13):
            inputstring += "1\n1\n1\n" + str(options[i]) + "\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                spiel = Spiel.Spiel()
                spiel.spielstarten()


import unittest

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
        self.assertEqual(type(thawed), type(block))
        self.assertEqual(block.gamened(), False)

    def testblockAusgabe(self):
        block: Block = Block.Spielblock()
        block.ausgabe("Steve", "Steve's Opfer'")

    def testinvalidSpielblock(self):
        block: Block = Block.Spielblock()
        block.punkteeinlesen(1, 0, False, 1, 1, 2, 3, 1)




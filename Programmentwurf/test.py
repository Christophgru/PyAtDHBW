
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


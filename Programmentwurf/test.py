import spiel as Spiel
#import spielblock as Block
import dice as Dice
import player as Player
#from io import StringIO
from unittest import TestCase


class TestSnackautomat3(TestCase):
    """
    todo: all: testet was das zeug hält
    """
    #def testSpiel(self):
        #spiel = Spiel.Spiel()


    #def testSpielStarten(self):
        #spiel = Spiel.Spiel()
        #self.assertTrue(spiel.spielstarten())

    #def testSpielblock(self):
        #block: Block = Block.Spielblock()
        #block.freeze(block)
        #thawed = block.thaw()

    def testPlayererstellen(self):
        myPlayer = Player.Player(True, "Ali")
        self.assertEqual(myPlayer.istecht, True)
        self.assertEqual(myPlayer.name, "Ali")


    def testDiceActivate(self):
        mydice = Dice.Dice()
        mydice.activate()
        self.assertIsNone(mydice.augen)
        self.assertTrue(mydice.isactivated)

    def testDiceDeactivate(self):
        mydice = Dice.Dice()
        mydice.deactivate()
        self.assertIsNone(mydice.augen)
        self.assertFalse(mydice.isactivated)

    def testDiceThrow(self):
        mydice = Dice.Dice()
        mydice.throw()
        #self.addTypeEqualityFunc(mydice.augen)
        self.assertIsNotNone(mydice.augen)

    def testDiceAlles(self):
        mydice = Dice.Dice()
        mydice.throw()
        mydice.activate()
        self.assertIsNotNone(mydice.augen)
        self.assertTrue(mydice.isactivated)
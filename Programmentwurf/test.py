import sys
import io
from unittest.mock import patch
import spiel as Spiel
#import spielblock as Block
import ui as Ui
import dice as Dice
import player as Player
from io import StringIO
from unittest import TestCase
import mock

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

    #def testui(self):
        #myUi = Ui.UI("da")
        #with mock.patch('builtins.input', return_value="2"):
            #assert myUi.pvp_or_pve()
            #self.assertTrue()


    def testuiwelcome(self):
        myUI = Ui.UI("da")
        myUI.welcome()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            myUI.welcome()
            self.assertEqual(fake_out.getvalue(), "Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen.\n"
              "Falls sie die Spielregeln noch nicht kennen google sie sie bitte .\n")

    def testuiendgame(self):
        myUI = Ui.UI("da")
        myUI.endgame("Ali", "Ali", "Elias")

    def testuichooseplayer(self):
        myUI = Ui.UI("da")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            myUI.chooseplayer("Ali")
            self.assertEqual(fake_out.getvalue(), "\n\n\nEs ist  Ali dran\n")


    def testausgabeui(self):
        myUI = Ui.UI("Da")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            myUI.chooseplayer("Christoph")
            self.assertEqual(fake_out.getvalue(), "\n\n\nEs ist  Christoph dran\n")

    def testuichoosename(self):
        myUI = Ui.UI("Da")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("Ali")) as fake_in:
                myUI.choosename(1)
                self.assertEqual(fake_out.getvalue(), "Spieler 1, bitte wählen sie ihren Namen")

    def testuipvp(self):
        myUI = Ui.UI("Da")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("1")) as fake_in:
                myUI.pvp_or_pve()
                self.assertEqual(fake_out.getvalue(), "Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                        "Wollen sie gegen einen Computer spielen drücken sie    : 2\n")

    def testuipve(self):
        myUI = Ui.UI("Da")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("2")) as fake_in:
                myUI.pvp_or_pve()
                self.assertEqual(fake_out.getvalue(), "Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                        "Wollen sie gegen einen Computer spielen drücken sie    : 2\n")

    #def testuipvpprobe(self):
        #myUI = Ui.UI("Da")
        #with patch('sys.stdout', new=StringIO()) as fake_out:
            #with patch('sys.stdin', new=StringIO("3")) as fake_in:
                #myUI.pvp_or_pve()
                #self.assertEqual(fake_out.getvalue(), "Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                        #"Wollen sie gegen einen Computer spielen drücken sie    : 2\n")
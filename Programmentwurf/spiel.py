import dice
import spielblock
import player


class Spiel:

    def __init__(self):
        # Todo:init
        self.dicedict: dict = {}
        for i in range(0, 4):
            self.dicedict[i] = dice.dice()
        self.boolPvP: bool = None
        self.spielblock: spielblock = spielblock
        self.nrround: int = 0
        self.activeplayer: int = 1
        self.player1: player.Player
        self.player2: player.Player

    def spielstarten(
            self):
        self.boolPvP = self.choosegamemode()
        # todo spieler initialisieren
        while not self.spielvorbei(False):
            self.wuerfeln()
            self.spielerwechsel()
        self.spielvorbei(True)

    def wuerfeln(self):
        """
          todo: würfeln, auswahl, nochmalwürfeln, Wahl (bsp full house...) tätigen, punkteeinlesen...
              """

    def spielvorbei(self, spielvorbei: bool):
        """
        todo: wenn param spielvorbei    = false->   schau ob noch weiter gespiel werden kann
                                                (alle felder ausgefüllt: abfrage Steve)
                                        =true->     Sieger ausgeben, (spiel speichern?)
        """

    def spielerwechsel(self):
        """
            todo anderen spieler aktivieren
               """

    def choosegamemode(self) -> bool:
        """
          todo: abfrage ob pvp oder pve, return tru if pvp else return false
              """

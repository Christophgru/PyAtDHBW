"""
ausgaben an Console nur ueber methoden in ui, um alle "oberflaechen aktionen" zu kapseln
"""

import dice
import spielblock
import player
import ui


class Spiel:

    def __init__(self):
        self.dicedict: dict = {}
        for i in range(0, 5):
            self.dicedict[i] = dice.Dice()
        self.boolPvP: bool = False
        self.spielblock: spielblock.Spielblock = spielblock.Spielblock()
        self.nrround: int = 0
        self.activeplayer: int = 0
        self.player1: player.Player = None
        self.player2: player.Player = None
        self.ui = ui.UI(self.spielblock)
        self.ui.welcome()

    def spielstarten(self):
        self.boolPvP = self.ui.pvp_or_pve()
        self.player1 = player.Player(True, self.ui.choosename(1))
        if self.boolPvP:
            self.player2 = player.Player(True, self.ui.choosename(2))
        else:
            self.player2 = player.Player(False, "E-Gegner")

        while not self.spielvorbei(False):
            self.wuerfeln()
            self.spielerwechsel()
        self.spielvorbei(True)
        return True

    def wuerfeln(self):
        """
          würfeln, auswahl, nochmalwürfeln, Wahl (bsp full house...) tätigen, punkteeintragen...
              """
        anzahlwuerfe = 1

        for j in range(0, len(self.dicedict)):  # Fuer jeden gewaehlten wuerfel wird einer mehr deaktiviert
            self.dicedict.get(j).activate()

        while anzahlwuerfe <= 3:  # anzahl w
            try:

                for j in range(0, len(self.dicedict)):  # Alle wuerfel werden gewuerfelt
                    wuerfelx = self.dicedict.get(j)
                    if wuerfelx.isactivated is True:
                        wuerfelx.throw()
                    else:
                        wuerfelx.deactivate()

                self.ui.choosediceorcheck(self.dicedict)
            except (KeyboardInterrupt, TypeError) as e:
                print("Keine Wuerfel ausgewaehlt")
                anzahlwuerfe -= 1
                break

            anzahlgewaehlt = 0
            for j in range(0, len(self.dicedict)):
                if not self.dicedict.get(j).isactivated:
                    anzahlgewaehlt += 1
            if anzahlgewaehlt == 5:
                anzahlwuerfe = 3
            anzahlwuerfe += 1

            # wenn loop vorbei und nicht alle wuerfel gewaehlt wurden, werden die restlichen wuerfel automatisch zugewiesen
            for j in range(0, 5):  # fuer jeden wuerfel, der noch nicht eingetragen wurde...
                if self.dicedict.get(j).isactivated:  # ...finde einen wuerfel, der noch aktiviert war
                    self.dicedict.get(j).activate()

        # waehle was eingetragen werden soll
        wahl = self.ui.choose_action_with_dice_arr(self.dicedict, self.spielblock, self.activeplayer)
        # wahl=self.nrround+1
        # packe würfelaugen in array zur übergabe an steve: punkteeinlesen()
        augenarray: list = [None, None, None, None, None]
        for k in range(0, len(self.dicedict)):
            augen = self.dicedict.get(k).augen
            if augen is None:
                augen = -1
            augenarray[k] = augen

        # gib das eingelesene an spielblock weiter

        self.spielblock.punkteeinlesen(wahl, self.activeplayer, self.ui.leer, *augenarray)

    def spielvorbei(self, spielvorbei: bool) -> bool:
        if not spielvorbei:
            return self.spielblock.gamened()
        else:
            if self.spielblock.endstand[0] > self.spielblock.endstand[1]:
                self.ui.endgame(self.player1.name)
            else:
                self.ui.endgame(self.player2.name)

    def spielerwechsel(self):
        if self.activeplayer == 0:
            self.activeplayer = 1
            self.ui.chooseplayer(self.player2.name)
            self.nrround = +1
        else:
            self.activeplayer = 0
            self.ui.chooseplayer(self.player1.name)

"""
ausgaben an Console nur ueber methoden in ui, um alle "oberflaechen aktionen" zu kapseln
"""

import dice
import spielblock
import player
import ui


class Spiel:

    def __init__(self):
        # Todo:init
        self.dicedict: dict = {}
        for i in range(0, 5):
            self.dicedict[i] = dice.Dice()
        self.boolPvP: bool = False
        self.spielblock: spielblock.Spielblock = spielblock.Spielblock()
        self.nrround: int = 0
        self.activeplayer: int = 1
        self.player1: player.Player = None
        self.player2: player.Player = None
        self.ui = ui.UI()
        self.ui.welcome()

    def spielstarten(self):
        self.boolPvP = self.choosegamemode()

        self.player1 = player.Player(True, "")
        if self.boolPvP:
            self.player2 = player.Player(True, "")
        else:
            self.player2 = player.Player(False, "")

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

        anzahlgewaehlt = 0
        for j in range(0, len(self.dicedict)):  # Fuer jeden gewaehlten wuerfel wird einer mehr deaktiviert
            self.dicedict.get(j).activate()

        while anzahlwuerfe <= 3:  # anzahl w
            try:

                for j in range(0, len(self.dicedict)):  # Fuer jeden gewaehlten wuerfel wird einer mehr deaktiviert
                    if self.dicedict.get(j).isactivated():
                        self.dicedict.get(j).throw()
                    else:
                        self.dicedict.get(j).deactivate()
                    # und einer weniger gewuerfelt

                self.ui.choosediceorcheck(self.dicedict)
            except (KeyboardInterrupt, TypeError) as e:
                print("Keine Wuerfel ausgewaehlt")
                anzahlwuerfe -= 1
                break
            anzahlwuerfe += 1

            for j in range(0, len(self.dicedict)):
                if self.dicedict.get(j).isactivated():
                    anzahlgewaehlt += 1

            # wenn loop vorbei und nicht alle wuerfel gewaehlt wurden, werden die restlichen wuerfel automatisch zugewiesen
            for j in range(0, 5):  # fuer jeden wuerfel, der noch nicht eingetragen wurde...
                dicex = None
                if self.dicedict.get(j).isactivated:  # ...finde einen wuerfel, der noch aktiviert war
                    dicex = self.dicedict.get(j)

        # waehle was eingetragen werden soll
        wahl = self.ui.choose_action_with_dice_arr(self.dicedict)

        # gib das eingelesene an spielblockblock weiter
        self.spielblock.punkteeinlesen(wahl, self.activeplayer, self.dicedict.values())


def spielvorbei(self, spielvorbei: bool) -> bool:
    """
    todo:yan wenn param spielvorbei    = false->   schau ob noch weiter gespiel werden kann
                                            (alle felder ausgefüllt: abfrage Steve)
                                    =true->     Sieger ausgeben, (spiel speichern?)
    """

    # anfrage steve:
    return self.spielblock.allezeilenvoll()


def spielerwechsel(self):
    """
        todo:yan  anderen spieler aktivieren, aufruf an ui um spieler zu informieren
           """


def choosegamemode(self) -> bool:
    """
      todo:yan abfrage ob pvp oder pve, return tru if pvp else return false
          """
    self.ui.pvp_or_pve()

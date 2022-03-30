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
        for i in range(0, 4):
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
        if self.ui.pvp_or_pve():
            self.player2 = player.Player(True, "")
        else:
            self.player2 = player.Player(False, "")

        while not self.spielvorbei(False):
            self.wuerfeln()
            self.spielerwechsel()
        self.spielvorbei(True)

    def wuerfeln(self):
        """
          würfeln, auswahl, nochmalwürfeln, Wahl (bsp full house...) tätigen, punkteeintragen...
              """
        gewaehltewuerfel: dict = {}
        anzahlwuerfe = 1

        for j in range(0, len(self.dicedict)):  # Fuer jeden gewaehlten wuerfel wird einer mehr deaktiviert
            self.dicedict.get(j).activate()

        while anzahlwuerfe <= 3:  # wuerfel waehlen
            try:
                for j in range(0, len(gewaehltewuerfel)):  # Fuer jeden gewaehlten wuerfel wird einer mehr deaktiviert
                    self.dicedict.get(j).deactivate()
                for j in range(len(gewaehltewuerfel), len(self.dicedict)):  # und einer weniger gewuerfelt
                    self.dicedict.get(j).throw()
                self.ui.choosediceorcheck(gewaehltewuerfel, self.dicedict)
                if len(gewaehltewuerfel) == 5:  # wenn alle wuerfel gewaehlt sind stopp
                    break
            except (KeyboardInterrupt,TypeError) as e:
                print("Keine Wuerfel ausgewaehlt")
                anzahlwuerfe -= 1
                break
            anzahlwuerfe += 1

        # wenn loop vorbei und nicht alle wuerfel gewaehlt wurden, werden die restlichen wuerfel automatisch zugewiesen
        if len(gewaehltewuerfel) < 5:
            k: int = 0  # nummer
            for j in range(len(gewaehltewuerfel) + 1, 5):  # fuer jeden wuerfel, der noch nicht eingetragen wurde...
                dicex = None
                while dicex is None and k <= 5:  # ...finde einen wuerfel, der noch aktiviert war
                    if self.dicedict.get(k).isactivated:
                        dicex = self.dicedict.get(k)
                    k += 1
                gewaehltewuerfel[j-1] = dicex  # und fuege diesen wuerfel als gewaehlt ein

        # waehle was eingetragen werden soll
        wahl = self.ui.choose_action_with_dice_arr(gewaehltewuerfel)

        # gib das eingelesene an spielblockblock weiter
        self.spielblock.punkteeinlesen(self.activeplayer, gewaehltewuerfel, wahl)

    def spielvorbei(self, spielvorbei: bool):
        """
        todo: wenn param spielvorbei    = false->   schau ob noch weiter gespiel werden kann
                                                (alle felder ausgefüllt: abfrage Steve)
                                        =true->     Sieger ausgeben, (spiel speichern?)
        """

    def spielerwechsel(self):
        """
            todo anderen spieler aktivieren, aufruf an ui um spieler zu informieren
               """

    def choosegamemode(self) -> bool:
        """
          todo: abfrage ob pvp oder pve, return tru if pvp else return false
              """

"""
ausgaben an Console nur ueber methoden in _ui, um alle "oberflaechen aktionen" zu kapseln
game-class-file
"""

import dice
import spielblock
import player
import ui


class Spiel:
    """
    game-class
    """

    def __init__(self):
        self.dicedict: dict = {}
        for i in range(0, 5):
            self.dicedict[i] = dice.Dice()
        self.spielblock: spielblock.Spielblock = spielblock.Spielblock()
        self.nrround: int = 0
        self.activeplayer: int = 0
        self.player1: player.Player  # einfügen
        self.player2: player.Player  # einfügen
        self._ui = ui.UI(self.spielblock)
        self._ui.welcome()

    def spielstarten(self):
        """

        @return:
        @rtype:
        """
        pvp: bool = self._ui.pvp_or_pve()
        self.player1 = player.Player(True, self._ui.choosename(1))
        if pvp:
            self.player2 = player.Player(True, self._ui.choosename(2))
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

        for j in range(0, len(self.dicedict)):  # Gewuerfelte wuerfel werden nicht nochmal
            self.dicedict.get(j).activate()

        while anzahlwuerfe <= 2:  # anzahl w

            self.throw()

            self.player2.choosediceorcheck(self.dicedict, self._ui, self.activeplayer)

            weiterspielen:bool = False
            for j in range(0, len(self.dicedict)):
                if self.dicedict.get(j).isactivated:
                    weiterspielen=True
            if not weiterspielen:
                anzahlwuerfe = 2
            anzahlwuerfe += 1



        #noch einmal wuerfeln
        self.throw()
        # waehle was eingetragen werden soll

        wahl = self.player2.choose_action_with_dice_arr({"activeplayer": self.activeplayer,
                                                         "nrround": self.nrround,
                                                         "ui": self._ui, "dicedict": self.dicedict,
                                                         "spielblock": self.spielblock,
                                                         "player1_name": self.player1.name})
        self._ui.clear()

        # wahl=self.nrround+1
        # packe würfelaugen in array zur übergabe an steve: punkteeinlesen()
        augenarray: list = [None, None, None, None, None]
        for k in range(0, len(self.dicedict)):
            augen = self.dicedict.get(k).augen
            if augen is None:
                augen = -1
            augenarray[k] = augen

        # gib das eingelesene an spielblock weiter

        self.spielblock.punkteeinlesen(wahl, self.activeplayer, self._ui.leer, *augenarray)
        self._ui.leer = False

    def throw(self):
        for j in range(0, len(self.dicedict)):  # Alle wuerfel werden gewuerfelt
            wuerfelx = self.dicedict.get(j)
            if wuerfelx.isactivated is True:
                wuerfelx.throw()
            else:
                wuerfelx.deactivate()

    def spielvorbei(self, spielvorbei: bool) -> bool:
        """

        @param spielvorbei:
        @type spielvorbei:
        @return:
        @rtype:
        """
        if not spielvorbei:
            return self.spielblock.gamened()
        if self.spielblock.endstand[0] > self.spielblock.endstand[1]:
            self._ui.endgame(self.player1.name, self.player1.name, self.player2.name)
        else:
            self._ui.endgame(self.player2.name, self.player1.name, self.player2.name)

    def spielerwechsel(self):
        """

        @return:
        @rtype:
        """
        if self.activeplayer == 0:
            self.activeplayer = 1
            self._ui.chooseplayer(self.player2.name)
            self.nrround += 1
        else:
            self.activeplayer = 0
            self._ui.chooseplayer(self.player1.name)

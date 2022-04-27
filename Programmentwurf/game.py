"""
ausgaben an Console nur ueber methoden in _ui, um alle "oberflaechen aktionen" zu kapseln
game-class-file
"""

import dice
import gameblock
import player
import ui


class Game:
    """
    game-class
    """

    def __init__(self):
        self.dicedict: dict = {}
        for i in range(0, 5):
            self.dicedict[i] = dice.Dice()
        self.gameblock: gameblock.Gameblock = gameblock.Gameblock()
        self.nrround: int = 0
        self.activeplayer: int = 0
        self.player1: player.Player  # einfügen
        self.player2: player.Player  # einfügen
        self._ui = ui.UI(self.gameblock)
        self._ui.welcome()

    def startgame(self):
        """

        @return:
        @rtype:
        """
        pvp: bool = self._ui.pvp_or_pve()
        self.player1 = player.Player(True, self._ui.choosename(1, None))
        if pvp:
            self.player2 = player.Player(True, self._ui.choosename(2, self.player1.name))
        else:
            self.player2 = player.Player(False, "E-Gegner")

        while not self.gameover(False):
            self.playround()
            self.switchplayer()
        self.gameover(True)
        return True

    def playround(self):
        """
          würfeln, auschoice, nochmalwürfeln, choice (bsp full house...) tätigen, punkteeintragen...
              """
        nrthrows = 1

        for j in range(0, len(self.dicedict)):  # Gewuerfelte wuerfel werden nicht nochmal
            self.dicedict.get(j).activate()

        while nrthrows <= 2:  # anzahl w

            self.throw()

            self.player2.choosediceorcheck(self.dicedict, self._ui, self.activeplayer)

            keep_playing: bool = False
            for j in range(0, len(self.dicedict)):
                if self.dicedict.get(j).isactivated:
                    keep_playing = True
            if not keep_playing:
                nrthrows = 2
            nrthrows += 1

        # noch einmal wuerfeln
        self.throw()
        # waehle was eingetragen werden soll

        choice = self.player2.choose_action_with_dice_arr({"activeplayer": self.activeplayer,
                                                           "nrround": self.nrround,
                                                           "ui": self._ui, "dicedict": self.dicedict,
                                                           "gameblock": self.gameblock,
                                                           "player1_name": self.player1.name})
        self._ui.clear()

        # choice=self.nrround+1
        # packe würfeleyes in array zur übergabe an steve: punkteeinlesen()
        eyesarray: list = [None, None, None, None, None]
        for k in range(0, len(self.dicedict)):
            eyes = self.dicedict.get(k).eyes
            if eyes is None:
                eyes = -1
            eyesarray[k] = eyes

        # gib das eingelesene an gameblock weiter

        self.gameblock.inputpoints(choice, self.activeplayer, self._ui.leer, *eyesarray)
        self._ui.leer = False

    def throw(self):
        """
        wuerfel wuerfeln
        @return:
        """
        for j in range(0, len(self.dicedict)):  # Alle wuerfel werden gewuerfelt
            dicex: dice.Dice = self.dicedict.get(j)
            if dicex.isactivated is True:
                dicex.throw()
            else:
                dicex.deactivate()

    def gameover(self, gameover: bool) -> bool:
        """

        @param gameover:
        @type gameover:
        @return:
        @rtype:
        """
        if not gameover:
            return self.gameblock.gamened()
        if self.gameblock.endstand[0] > self.gameblock.endstand[1]:
            self._ui.endgame(self.player1.name, self.player1.name, self.player2.name)
        else:
            self._ui.endgame(self.player2.name, self.player1.name, self.player2.name)
        return False

    def switchplayer(self):
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

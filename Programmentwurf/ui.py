"""
user-interface-class-file
"""
import string
import os
import gameblock


class UI:
    """
    User-interface-class
    """

    def __init__(self, s_b: gameblock.Gameblock):
        self.output = None
        self.gameblock = s_b
        self.leer = False
        self.maxequal = 1
        self.secondequal = 1
        self.kniffel = {0: False, 1: False}

    @classmethod
    def choosename(cls, playernumber: int, playername: string) -> string:
        """

        @param playername: Name of the first Player  or None
        @param playernumber: Number of the aktive Player
        @type playernumber: int
        @return: Playername
        @rtype: string
        """
        name = None
        run = True
        while run:
            readin: string = "Spieler " + str(playernumber) + ", bitte wählen sie ihren Namen"
            name = input(readin)
            if playername is not None:
                if name == playername:
                    print("Geben sie bitte einen Namen ein, der sich vom Namen des 1. Spielers unterscheidet.")
                else:
                    run = False
            else:
                run = False
        return name

    @classmethod
    def pvp_or_pve(cls) -> bool:
        """

        @return: bool if PvP or PvE
        @rtype: bool
        """
        while True:
            ret = input("Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                        "Wollen sie gegen einen Computer spielen drücken sie    : 2\n")
            match ret:
                case '1':
                    return True
                case '2':
                    return False
                case _:
                    print("Geben sie bitte nur 1 oder 2 ein")

    @classmethod
    def choosediceorcheck(cls, dice_in_cup: dict):
        """
        check which dices the Player want to change
        @param dice_in_cup: all Dices
        @type dice_in_cup: dict
        @return: -
        @rtype: -
        """
        again = True
        while again:
            again = False
            print("Gewählte Würfel:\n")
            i = 1
            for wuerfel in dice_in_cup.values():
                if not wuerfel.isactivated:
                    print("Würfel", i, ":", wuerfel.eyes)
                i += 1

            print("\nGewürfelte Würfel:\n")
            i = 1
            for wuerfelx in dice_in_cup.values():
                if wuerfelx.isactivated:
                    print("Würfel", i, ":", wuerfelx.eyes)
                i += 1

            eing = input("Wollen Sie schon ausgewählte Würfel wieder in den Becher werfen, \n"
                         "oder gewürfelte Würfel beiseite legen, dann geben Sie bitte den Würfelindex ein \n"
                         "Bei mehreren Würfeln den Würfelindex bitte ohne Leerzeichen eingeben und mit Komma trennen\n"
                         "Wenn sie nichts auswählen möchten geben sie 0 ein.\n")
            eing = eing.split(",")
            for choosen_dice in eing:
                if choosen_dice in ("1", "2", "3", "4", "5"):
                    if dice_in_cup[int(choosen_dice) - 1].isactivated:
                        dice_in_cup[int(choosen_dice) - 1].deactivate()
                    else:
                        dice_in_cup[int(choosen_dice) - 1].activate()
                elif choosen_dice != "0":
                    print("Wählen sie bite bloß 1,2,3,4 oder 5 aus")
                    again = True

    def choose_action_with_dice_arr(self, params: dict) -> int:
        """
        User interaction to chooce the line of the block
        @param params: dices, gameblock, aktive Playernumber, both Playernames, bool if PvE
        @return: linenumber
        """

        wuerfelobjekte: dict = params["dicedict"]
        block: gameblock.Gameblock = params["gameblock"]
        playernumber: int = params["activeplayer"]
        namenarr: string = params["playernames"]
        is_pve = params["isPVE"]

        augenarray = [wuerfelobjekte[0].eyes, wuerfelobjekte[1].eyes, wuerfelobjekte[2].eyes,
                      wuerfelobjekte[3].eyes, wuerfelobjekte[4].eyes]
        self.gameblock.output(namenarr[0], namenarr[1], *augenarray)
        sortdice = sorted(augenarray)
        self.getequals(sortdice)
        self.checkbonus(playernumber)
        while True:
            while True:
                try:
                    _eing = input("Geben sie bitte die Zeile an in welche sie das Gewürfelte eintragen wollen\n")
                    _eingabe = int(_eing)
                except ValueError:
                    print("Geben sie bloß Zahlen ein\n")
                    break
                if _eingabe < 1 or _eingabe > 16 or _eingabe in (7, 8, 9):
                    print("Geben sie nur Zahlen zwischen 1 und 6 oder 10 und 16 ein\n")
                    break
                if _eingabe < 7:
                    if block.first_line[_eingabe - 1][playernumber]:
                        print("Zeile bereits gefüllt")
                        break
                    return _eingabe
                if _eingabe == 16:
                    if block.second_line[_eingabe - 10][playernumber]:
                        print("Zeile bereits gefüllt")
                        break
                    return _eingabe
                if _eingabe > 9:
                    if block.second_line[_eingabe - 10][playernumber]:
                        print("Zeile bereits gefüllt")
                        break
                if self.checkline(sortdice, _eingabe):
                    if _eingabe == 15:
                        self.kniffel[playernumber] = True
                    return _eingabe
                _einga = self.zeroline(is_pve)
                if _einga == '0':
                    self.leer = True
                    return _eingabe

    @classmethod
    def chooseplayer(cls, playername):
        """

        @param playername: aktive Playername
        @type playername: string
        @return: -
        @rtype: -
        """
        print("\n\n\nEs ist ", playername, "dran")

    def endgame(self, winner, name1, name2):
        """

        @param name2: Player 2 Name
        @param name1: Player 1 Name
        @param winner: Name of the Winner
        @type winner: string
        @return: -
        @rtype: -
        """
        self.gameblock.output(name1, name2)
        print("Der Gewinner ist", winner)

    @classmethod
    def welcome(cls):
        """
        welcome text
        @return:
        @rtype:
        """
        print("Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen.\n"
              "Falls sie die Spielregeln noch nicht kennen google sie sie bitte.")

    @classmethod
    def clear(cls):
        """
        clear the console
        @return:
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def checkline(self, sortdice, _eingabe):
        """

        @param sortdice: sorted dices
        @param _eingabe: the line which should be checked
        @return: -
        """
        check = False
        match _eingabe:
            case 10:
                if self.maxequal > 2:
                    check = True
            case 11:
                if self.maxequal > 3:
                    check = True
            case 12:
                if self.maxequal == 3 and self.secondequal == 2:
                    check = True
            case 13:
                count = 1

                for i in range(len(sortdice) - 1):
                    if sortdice[i] == sortdice[i + 1] - 1:
                        count += 1
                    elif not sortdice[i] == sortdice[i + 1]:
                        count = 1
                if count >= 4:
                    check = True

            case 14:
                if self.maxequal == 1 and ((sortdice[0] == 1) ^ (sortdice[len(sortdice) - 1] == 6)):
                    check = True
            case 15:
                if self.maxequal == 5:
                    check = True
        return check

    def getequals(self, sortdice):
        """

        @param sortdice: sorted Dices
        @return:
        """
        self.maxequal = 1
        self.secondequal = 1
        for i in range(len(sortdice) - 1):
            if sortdice[i] == sortdice[i + 1]:
                if sortdice[0] == sortdice[i]:
                    self.maxequal += 1
                else:
                    self.secondequal += 1
                if self.maxequal < self.secondequal:
                    self.maxequal, self.secondequal = self.secondequal, self.maxequal

    @classmethod
    def checkpve(cls, is_pve: bool):
        """

        @param is_pve: if its PvE
        @type is_pve:bool
        @return: -
        @rtype: -
        """
        if not is_pve:
            _einga = input("Sie haben nicht die Anforderungen für diese Zeile!\n"
                           "Wenn sei 0 Punkte eintragen möchten geben sie 0 ein\n"
                           "Für eine neue Auswahl geben sie etwas anders ein")
        else:
            _einga = '0'
        return _einga

    @classmethod
    def zeroline(cls, pve: bool) -> string:
        if not pve:
            _einga = input("Sie haben nicht die Anforderungen für diese Zeile!\n"
                           "Wenn sei 0 Punkte eintragen möchten geben sie 0 ein\n"
                           "Für eine neue Auswahl geben sie etwas anders ein")
        else:
            _einga = '0'
        return _einga

    def checkbonus(self, playernumber: int):
        if self.maxequal == 5:
            if self.kniffel[playernumber]:
                self.gameblock.pluskniffel(playernumber)

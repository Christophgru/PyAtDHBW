"""
#todo
"""
import string
import os
import spielblock


class UI:
    """
    User-interface-class
    """

    def __init__(self, s_b: spielblock.Spielblock):
        self.output = None
        self.spielblock = s_b
        self.leer = False

    @classmethod
    def choosename(cls, playernumber) -> string:
        """

        @param playernumber:
        @type playernumber:
        @return:
        @rtype:
        """
        aufforderung: string = "Spieler " + str(playernumber) + ", bitte wählen sie ihren Namen"
        name = input(aufforderung)
        return name

    @classmethod
    def pvp_or_pve(cls) -> bool:
        """

        @return:
        @rtype:
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
    def choosediceorcheck(cls, wuerfel_im_becher: dict):
        """

        @param wuerfel_im_becher:
        @type wuerfel_im_becher:
        @return:
        @rtype:
        """
        again = True
        while again:
            again = False
            print("Gewählte Würfel:\n")
            i = 1
            for wuerfel in wuerfel_im_becher.values():
                if not wuerfel.isactivated:
                    print("Würfel", i, ":", wuerfel.augen)
                i += 1

            print("\nGewürfelte Würfel:\n")
            i = 1
            for wuerfelx in wuerfel_im_becher.values():
                if wuerfelx.isactivated:
                    print("Würfel", i, ":", wuerfelx.augen)
                i += 1

            eing = input("Wollen Sie schon ausgewählte Würfel wieder in den Becher werfen, \n"
                         "oder gewürfelte Würfel beiseite legen, dann geben Sie bitte den Würfelindex ein \n"
                         "Bei mehreren Würfeln den Würfelindex bitte ohne Leerzeichen eingeben und mit Komma trennen\n"
                         "Wenn sie nichts auswählen möchten geben sie 0 ein.\n")
            eing = eing.split(",")
            for choosen_dice in eing:
                if choosen_dice in ("1", "2", "3", "4", "5"):
                    if wuerfel_im_becher[int(choosen_dice) - 1].isactivated:
                        wuerfel_im_becher[int(choosen_dice) - 1].deactivate()
                    else:
                        wuerfel_im_becher[int(choosen_dice) - 1].activate()
                elif choosen_dice != "0":
                    print("Wählen sie bite bloß 1,2,3,4 oder 5 aus")
                    again = True

    def choose_action_with_dice_arr(self, wuerfelobjekte: dict, block: spielblock.Spielblock, playernumber: int,
                                    name1: string, name2: string) -> int:
        """

        @param name2:
        @param name1:
        @param wuerfelobjekte:
        @type wuerfelobjekte:
        @param block:
        @type block:
        @param playernumber:
        @type playernumber:
        @return:
        @rtype:
        """
        self.spielblock.ausgabe(name1, name2)

        augenarray = [wuerfelobjekte[0].augen, wuerfelobjekte[1].augen, wuerfelobjekte[2].augen,
                      wuerfelobjekte[3].augen, wuerfelobjekte[4].augen]
        while True:
            while True:
                try:
                    _eing = input("Geben sie bitte die Zeile an in welche sie das Gewürfelte eintragen wollen\n")
                    _eingabe = int(_eing)
                except ValueError:
                    print("Geben sie bloß Zahlen ein\n")
                    break
                if _eingabe in (7, 8, 9, 17, 18, 19):
                    print("Geben sie bitte mögliche Zeilen ein, alle außer 7,8,9,17,18,19\n")
                    break
                if _eingabe < 1 or _eingabe > 19:
                    print("Geben sie nur Zahlen zwischen 1 und 19 ein\n")
                    break
                if _eingabe < 7 or _eingabe == 16:
                    if block.first_line[_eingabe - 1][playernumber]:
                        print("Zeile bereits gefüllt")
                        break
                    return _eingabe
                if _eingabe > 9:
                    if block.second_line[_eingabe - 10][playernumber]:
                        print("Zeile bereits gefüllt")
                        break
                sortdice = sorted(augenarray)
                maxequal = 1
                secondequal = 1
                equal = 1
                check = False
                for i in range(len(sortdice) - 1):
                    if i != range(len(sortdice)):
                        if sortdice[i] == sortdice[i + 1]:
                            equal += 1
                            if maxequal < equal:
                                maxequal = equal
                            elif maxequal != equal:
                                secondequal = equal
                        else:
                            equal = 1
                match _eingabe:
                    case 10:
                        if maxequal > 2:
                            check = True
                    case 11:
                        if maxequal > 3:
                            check = True
                    case 12:
                        if (maxequal == 3 and secondequal == 2) or maxequal == 5:
                            check = True
                    case 13:
                        count = 1

                        for i in range(len(sortdice) - 1):
                            if sortdice[i] == sortdice[i + 1] - 1:
                                count += 1
                            else:
                                if not sortdice[i] == sortdice[i+1]:
                                    count = 1
                        if count >= 4:
                            check = True

                    case 14:
                        if maxequal == 1 and sortdice[0] == 1 or sortdice[len(sortdice) - 1] == 6:
                            check = True
                    case 15:
                        if maxequal == 5:
                            check = True
                if check:
                    return _eingabe
                else:
                    _einga = input("Sie haben nicht die Anforderungen für diese Zeile!\n"
                                   "Wenn sei 0 Punkte eintragen möchten geben sie 0 ein\n"
                                   "Für eine neue Auswahl geben sie etwas anders ein")
                    if _einga == '0':
                        self.leer = True
                        return _eingabe

    @classmethod
    def chooseplayer(cls, playername):
        """

        @param playername:
        @type playername:
        @return:
        @rtype:
        """
        print("\n\n\nEs ist ", playername, "dran")

    def endgame(self, winner, name1, name2):
        """

        @param name2:
        @param name1:
        @param winner:
        @type winner:
        @return:
        @rtype:
        """
        self.spielblock.ausgabe(name1, name2)
        print("Der Gewinner ist", winner)

    @classmethod
    def welcome(cls):
        """

        @return:
        @rtype:
        """
        print("Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen.\n"
              "Falls sie die Spielregeln noch nicht kennen google sie sie bitte .")

    @classmethod
    def clear(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

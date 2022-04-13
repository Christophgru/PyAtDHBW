# todo elias
import string
import spielblock
import spiel
import dice


class UI:
    def __init__(self, sb: spielblock.Spielblock):
        self.output = None
        self.spielblock = sb

    def choosename(self, playernumber) -> string:
        name = input(print("Spieler ", playernumber, ", bitte wählen sie ihren Namen"))
        return name

    def pvp_or_pve(self) -> bool:
        """
               """
        while True:
            ret = input("Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                        "Wollen sie gegen einen Computer spielen drücken sie    : 2\n")
            if ret == '1':
                return True
            elif ret == '2':
                return False
            else:
                print("Geben sie bitte nur 1 oder 2 ein")

    def choosediceorcheck(self, wuerfel_im_becher: dict):
        """
            todo: Elias: waehle aus gewuerfelte_wuerfel_dict aus den aktiven wuerfeln (dice.isactivated->bool) die
            passenden aus
            Fuege die gewaehlten wuerfel zum schon_gewaehlte_wuerfel_dict hinzu. Änderungen hier gelten auch
            im Hauptprogramm, deshalb keine rückgabe notwendig
            """
        again = True
        while again:
            again = False
            print("Gewählte Würfel:\n")
            q = 1
            for wuerfel in wuerfel_im_becher.values():
                if not wuerfel.isactivated:
                    print(q, ":", wuerfel.augen)
                q += 1

            print("\nGewürfelte Würfel:\n")
            q = 1
            for wuerfelx in wuerfel_im_becher.values():
                if wuerfelx.isactivated:
                    print(q, ":", wuerfelx.augen)
                q += 1
            eing = input("Wollen Sie schon ausgewählte Würfel wieder in den Becher werfen, \n"
                         "oder gewürfelte Würfel beiseite legen, dann geben Sie bitte den Würfelindex ein \n"
                         "Bei mehreren Würfeln den Würfelindex bitte ohne Leerzeichen eingeben und mit Komma trennen\n"
                         "Wenn sie nichts auswählen möchten geben sie 0 ein.\n")
            eing = eing.split(",")
            for x in eing:
                if x == "1" or x == "2" or x == "3" or x == "4" or x == "5":
                    if wuerfel_im_becher[int(x) - 1].isactivated:
                        wuerfel_im_becher[int(x) - 1].deactivate()
                    else:
                        wuerfel_im_becher[int(x) - 1].activate()
                elif x != "0":
                    print("Wählen sie bite bloß 1,2,3,4 oder 5 aus")
                    again = True

    def choose_action_with_dice_arr(self, wuerfelarray: dict, block: spielblock.Spielblock, playernumber: int) -> int:
        """
               """
        self.spielblock.ausgabe()
        while True:
            try:
                x = input("Geben sie bitte die Zeile an in welche sie das Gewürfelte eintragen wollen\n")
                x = int(x)
                break
            except ValueError:
                print("Geben sie bloß Zahlen ein\n")
        while True:
            if x == 7 or x == 8 or x == 9 or x == 17 or x == 18 or x == 19:
                print("Geben sie bitte mögliche Zeilen ein, alle außer 7,8,9,17,18,19\n")
            elif x < 1 or x > 19:
                print("Geben sie nur Zahlen zwischen 1 und 19 ein\n")
            if x < 7:
                if block.first_line[x - 1][playernumber]:
                    print("Zeile bereits gefüllt")
                else:
                    break
            if x > 9:
                if block.second_line[x - 10][playernumber]:
                    print("Zeile bereits gefüllt")
                else:
                    break
            sortdice = sorted(wuerfelarray)
            maxequal = 0
            secondequal = 0
            equal = 1
            for q in range(len(sortdice)):
                if q != range(len(sortdice)):
                    if sortdice[q] == sortdice[q + 1]:
                        equal += 1
            if maxequal < equal:
                maxequal = equal
            elif maxequal != equal:
                secondequal = equal

            if x == 10:
                if maxequal > 2:
                    return x
            elif x == 11:
                if maxequal > 3:
                    return x
            elif x == 12:
                if maxequal == 3 and secondequal == 2:
                    return x

            elif x == 13:
                count = 0
                for i in range(len(sortdice)):
                    if sortdice[i] == sortdice[i+1]-1:
                        count += 1
                if count <= 4:
                    return x

                return x
            elif x == 14:
                if maxequal == 1 and sortdice[0] == 1 or sortdice[len(sortdice)-1] == 6:
                    return x
            elif x == 15:
                if maxequal == 5:
                    return x
            elif x == 16:
                return x
        q = input("Sie haben nicht die Anforderungen für diese Zeile!\n"
                  "Wenn sei 0 Punkte eintragen möchten geben sie 0 ein\n"
                  "Für eine neue Auswahl geben sie etwas anders ein")
        if q == '0':
            for i in range(len(spiel.Spiel.dicedict)):
                spiel.Spiel.dicedict[i].augen = 0
            return x


def chooseplayer(self, playername):
    print("\n\n\nEs ist ", playername, "dran")


def endgame(self, winner):
    self.spielblock.ausgabe()
    print("Der Gewinner ist", winner)


def welcome(self):
    """

    """
    print("Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen.\n"
          "Falls sie die Spielregeln noch nicht kennen google sie sie bitte .")

# todo elias
import string
import spielblock


class UI:
    def __init__(self, sb:spielblock.Spielblock):
        self.output = None
        self.spielblock=sb

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
            eing = input("Wollen sie schon ausgewählte Würfek wieder in den Becher werfen \n"
                         "oder gewürfelte Würfel beiseite legen, dann geben si ebitte den Würfelindex ein \n"
                         "Bei mehreren Würfeln den Würfelindex bitte ohne Leerzeichen eingeben und mit Komma trennen\n")
            eing = eing.split(",")
            for x in eing:
                if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                    if wuerfel_im_becher[int(x)-1].isactivated:
                        wuerfel_im_becher[int(x)-1].deactivate()
                    else:
                        wuerfel_im_becher[int(x)-1].activate()
                elif x != 0:
                    print("Wählen sie bite bloß 1,2,3,4 oder 5 aus")
                    again = True


    def choose_action_with_dice_arr(self, wuerfelarray:dict) -> int:
        """
           todo: Elias:abfrage an user was mit den gewürfelten würfeln eingetragen werden soll. rückgabe int/string mit steve
           absprechen, je nachdem was er haben will um zeile zu identifizieren
               """
        self.spielblock.ausgabe()
        while True:
            try:
                x = input("Geben sie bitte die Zeile an in welche sie das Gewürfelte eintragen wollen")
                x = int(x)
                break
            except ValueError as e:
                print("Geben sie bloß Zahlen ein")
            if x == 7 or x == 8 or x == 9 or x == 17 or x == 18 or x == 19:
                print("Geben sie bitte mögliche Zeilen ein, alle außer 7,8,9,17,18,19")
            elif x < 1 or x > 19:
                print("Geben sie nur Zahlen zwischen 1 und 19 ein")
        return x

    def chooseplayer(self, playername):
        print("Es ist ", playername, "dran")

    def endgame(self, winner):
        self.spielblock.ausgabe()
        print("Der Gewinner ist", winner)

    def welcome(self):
        """todo: Elias: ausgabe: herzlich willkommen, spielregeln usw."""
        print("Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen.\n"
              "Falls sie die Spielregeln noch nicht kennen google sie sie bitte .")

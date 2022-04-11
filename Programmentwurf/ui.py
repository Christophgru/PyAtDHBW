# todo elias


class UI:
    def __init__(self):
        self.output = None

    def pvp_or_pve(self) -> bool:
        """
               """
        while True:
            ret = input(print("Wollen sie gegen eine andere Person spielen drücken sie: 1\n"
                              "Wollen sie gegen einen Computer spielen drücken sie    : 2\n"))
            if ret == '1':
                return True
            elif ret == '2':
                return False
            else:
                print("Geben sie bitte nur 1 oder 2 ein")

    def choosediceorcheck(self, schon_gewaehlte_wuerfel_dict: dict, wuerfel_im_becher: dict):
        """
            todo: Elias: waehle aus gewuerfelte_wuerfel_dict aus den aktiven wuerfeln (dice.isactivated->bool) die
            passenden aus
            Fuege die gewaehlten wuerfel zum schon_gewaehlte_wuerfel_dict hinzu. Änderungen hier gelten auch
            im Hauptprogramm, deshalb keine rückgabe notwendig
            """
        print("Gewählte Würfel:\n")
        q = 1
        for wuerfel in wuerfel_im_becher.values():
            if wuerfel.isdeactivated:
                print(q, ":", wuerfel.augen)
            q += 1

        print("\nGewürfelte Würfel:\n")
        q = 1
        for wuerfelx in wuerfel_im_becher.values():
            if wuerfelx.isactivated:
                print(q, ":", wuerfelx.augen)
            q += 1
        x = input(print("Wollen sie schon ausgewählte Würfek wieder in den Becher werfen?"
                        "Falls Nein geben sie 0 ein, ansosnen den Würfelindex"))


    def choose_action_with_dice_arr(self, dict) -> int:
        """
           todo: Elias:abfrage an user was mit den gewürfelten würfeln eingetragen werden soll. rückgabe int/string mit steve
           absprechen, je nachdem was er haben will um zeile zu identifizieren
               """

    def welcome(self):
        """todo: Elias: ausgabe: herzlich willkommen, spielregeln usw."""
        print("Herzlich willkommen bei Kniffel, sie können Player vs Player oder Player vs Computer spielen."
              "Falls sie die Spielregeln noch nicht kennen google sie sie bitte .")

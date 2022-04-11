# todo elias


class UI:
    def __init__(self):
        self.output = None

    def pvp_or_pve(self) -> bool:
        """
               todo: Elias: abfrage ob pvp oder pve, return true if pvp
               """

    def choosediceorcheck(self, schon_gewaehlte_wuerfel_dict: dict, wuerfel_im_becher: dict):
        """
            todo: Elias: waehle aus gewuerfelte_wuerfel_dict aus den aktiven wuerfeln (dice.isactivated->bool) die
            passenden aus
            Fuege die gewaehlten wuerfel zum schon_gewaehlte_wuerfel_dict hinzu. Änderungen hier gelten auch
            im Hauptprogramm, deshalb keine rückgabe notwendig
                """

        # um das programm zu testen habe ich (christoph) einfach immer den ersten noch aktiven würfel ausgewählt
        for wuerfelx in wuerfel_im_becher.values():
            if wuerfelx.isactivated:
                schon_gewaehlte_wuerfel_dict[len(schon_gewaehlte_wuerfel_dict)] = wuerfelx
                wuerfelx.deactivate()
                break

    def choose_action_with_dice_arr(self, wuerfelarray:dict) -> int:
        """
           todo: Elias:abfrage an user was mit den gewürfelten würfeln eingetragen werden soll. rückgabe int/string mit steve
           absprechen, je nachdem was er haben will um zeile zu identifizieren
               """

    def welcome(self):
        """todo: Elias: ausgabe: herzlich willkommen, spielregeln usw."""

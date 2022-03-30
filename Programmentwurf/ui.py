# todo elias



class UI:
    def __init__(self):
        self.output = None

    def pvp_or_pve(self) -> bool:
        """
               todo: abfrage ob pvp oder pve, return true if pvp
               """

    def choosediceorcheck(self, schon_gewaehlte_wuerfel_dict: dict, gewuerfelte_wuerfel_dict: dict):
        """
            todo: waehle aus gewuerfelte_wuerfel_dict ais den aktiven wuerfeln (dice.isactivated->bool) die passenden aus
            Fuege die gewaehlten wuerfel zum schon gewaehlte wuerfel dict hinzu, und gib dieses zurück
                """

        # um das programm zu testen habe ich (christoph) einfach immer den ersten noch aktiven würfel ausgewählt
        for wuerfelx in gewuerfelte_wuerfel_dict.values():
            if wuerfelx.isactivated:
                schon_gewaehlte_wuerfel_dict[len(schon_gewaehlte_wuerfel_dict)] = wuerfelx
                wuerfelx.deactivate()
                break

    def choose_action_with_dice_arr(self, dict) -> int:
        """
           todo:abfrage an user was mit den gewürfelten würfeln eingetragen werden soll. rückgabe int/string mit steve
           absprechen, je nachdem was er haben will um zeile zu identifizieren
               """

    def welcome(self):
        """todo ausgabe: herzlich willkommen, spielregeln usw."""

#todo elias

class UI:
    def __init__(self):
        self.output = None

    def pvp_or_pve(self) -> bool: """
        #todo: abfrage ob pvp oder pve, return true if pvp
        """

    def choosediceorcheck(self, schon_gewaehlte_wuerfel_dict: dict, gewuerfelte_wuerfel_dict: dict) -> dict:
        """
            waehle aus gewuerfelte_wuerfel_dict ais den aktiven wuerfeln (dice.isactivated->bool) die passenden aus
            Fuege die gewaehlten wuerfel zum schon gewaehlte wuerfel dict hinzu, und gib dieses zurück
                """


    def choose_action_with_dice_arr(self, dict) -> int: """
    abfrage an user was mit den gewürfelten würfeln eingetragen werden soll. rückgabe int/string was steve haben will
    um zeile zu identifizieren
        """

    def welcome(self): """ausgabe herzlich willkommen, spielregeln usw."""

#todo: yannic

class Player:
    def __init__(self, istecht: bool, name: str):
        self.istecht: bool = istecht
        self.name: str = name

    def wuerfelwaehlen(self, wuerfelarr: dict) -> list:
        """
        todo: bekommt die wuerfel, soll auswaehlen welche würfel genommen werden, gibt diese zurück
        """

    def eintragwaehlen(self, wuerfelarr: dict) -> int:
        """ todo: bekommt wuerfel in array in finaler position waehlt aus was damit gemacht werden soll (), gibt int zurück,
    wo die punkte eingetragen werden sollen

        """

class Tabelle:
    spieler: int
    kat: int = 10
    anzahlspiele: int
    block: int[anzahlspiele][kat]
    zeilenzuweisung = {"einser": 1, "zweier": 2, "dreier": 3, "vierer": 4, "fünfer": 5, "sechser": 6,"zahlenteilsumme":7, "Bonus bei mehr als 63":8,}

    def eintagvornehmen(self, spiel: int, typ: str, eintrag: int):
        indexzeile = self.zeilenzuweisung[typ]
        if self.block[spiel][indexzeile] is not None:
            return False
        self.block[spiel][indexzeile] = eintrag
        return True

    def getpunkte(self):
        return


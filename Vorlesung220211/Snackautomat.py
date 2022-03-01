from os import kill

eingezahlt: float = 0.0
status: int = 0
angebot = {
    1: ["Snickers1", 2, 1.20],
    2: ["Snickers2", 2, 1.20],
    3: ["Snickers3", 2, 1.20],
    4: ["Snickers4", 2, 1.20],
    5: ["Snickers5", 2, 1.20],
    6: ["Mars1    ", 2, 1.50],
    7: ["Mars2    ", 2, 1.50],
    8: ["Mars3    ", 2, 1.50],
    9: ["Mars4    ", 2, 1.50],
    10: ["Mars5   ", 2, 1.50]}


def einzahlen():
    # extra Methode um eventuell komplexe Finanztransaktiononen zu kapseln
    global eingezahlt
    eingezahlt += float(input("Wie viel möchten sie Einzahlen"))


def produktwaehlen() -> int:
    for i in range(1, 11):
        print(i, " : ", angebot[i][0], " ", angebot[i][1], "stück verfügbar für ", angebot[i][2], " €")
    try:
        num = int(input("Welches Produkt möchten Sie wählen (1-10)?"))
        if 0 > num > 10:
            kill()
        return num
    finally:
        print("ungültige eingabe")
        main()


def analyzeinput(key, aktuellerstatus) -> int:
    if key == "Y" or key == "y":
        return 1
    elif key == "W" or key == "w":
        return 2
    elif key == "A" or key == "a":
        return 6
    elif key == "K" or key == "k":
        print("Ihr aktueller Kontostand beträgt " + str(eingezahlt) + "€")
        return aktuellerstatus
    else:
        print("Leider konnten wir ihre Eingabe nicht verstehen.\nBitte versuchen Sie es erneut.")
        return aktuellerstatus


def main():
    global status
    global eingezahlt
    global angebot
    while status != -1:
        if status == 0:
            print("Herzlich Wilkommen am schnieken Snackautomaten")
            status = 1
        if status == 1:
            einzahlen()
            analyzeinput("K", 2)
            status = 2
        if status == 2:
            produktnummer = int(produktwaehlen())
            produkt = angebot.get(produktnummer)
            if produkt == None:
                print("ungültige eingabe")
                main()
            preis = float(produkt[2])
            anzahl = int(produkt[1])
            if eingezahlt >= preis and anzahl > 0:
                status = 3
            else:
                status = 4
        if status == 3:
            # Produkt ist bezahlbar und wird gekauft
            print("Hier haben Sie ihren " + produkt[0] + "\nVielen Dank für ihren Einkauf")
            eingezahlt -= preis
            print("Ihr restguthaben beträgt " + str(eingezahlt) + "€")
            angebot[produktnummer] = [produkt[0], produkt[1] - 1, produkt[2]]
            status = 5
        if status == 4:
            # Produkt ist zu teuer und wir nicht gekauft
            if anzahl == 0:
                print("Oh nein, das Produkt ist ausverkauft.")
            else:
                print("Oh nein, das Produkt istz zu teuer.")
            key = input("Um mehr Geld einzuzahlen drücken Sie <Y/y>\n"
                        "Um ein anderes Produkt zu wählen drücken Sie <W/w>\n"
                        "Um den Kontostand anzuzeigen drücken Sie <K/k>\n"
                        "Um den Kaufvorgang abzubrechen drücken Sie <A/a>")
            status = analyzeinput(key, status)
        if status == 5:
            # möchten Sie abbrechen oder weitere Produkte kaufen
            key = input(
                "Möchten Sie abbrechen <A/a>, den Kontostand anzeigen lassen <K/k> oder weitere Produkte kaufen <W/w>")
            status = analyzeinput(key, status)
        if status == 6:
            print("Ihr restguthaben in Höhe von " + str(eingezahlt) + "€ wurde ausgezahlt.\n"
                                                                      "Einen Schönen tag noch und bis nächstes Mal")
            status = -1


if __name__ == "__main__":
    main()

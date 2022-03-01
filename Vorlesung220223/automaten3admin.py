import snackautomat3

sortimentliste = {
    1: {"name": "Snickers1", "anzahl": 2, "preis": 1.20},
    2: {"name": "Snickers2", "anzahl": 2, "preis": 1.20},
    3: {"name": "Snickers3", "anzahl": 2, "preis": 1.20},
    4: {"name": "Snickers4", "anzahl": 2, "preis": 1.20},
    5: {"name": "Snickers5", "anzahl": 2, "preis": 1.20},
    6: {"name": "Mars1", "anzahl": 2, "preis": 1.80},
    7: {"name": "Mars2", "anzahl": 2, "preis": 1.80},
    8: {"name": "Mars3", "anzahl": 2, "preis": 1.80},
    9: {"name": "Mars4", "anzahl": 2, "preis": 1.80},
    10: {"name": "Mars5", "anzahl": 2, "preis": 1.80}}
userverzeichnis = {
    1: {"name": "Christoph", "passwort": "hello"},
    2: {"name": "Test",  "passwort": "hello"},
}


def zuruecksetzten():
    produkt_liste: dict = {}
    for i in range(1, len(sortimentliste)+1):
        produkt_liste[i] = snackautomat3.Product(sortimentliste[i]["name"], sortimentliste[i]["anzahl"],
                                                 sortimentliste[i]["preis"], i)

    user_liste: dict = {}
    for i in range(1, len(userverzeichnis)+1):
        user_liste[i] = snackautomat3.User(userverzeichnis[i]["name"],
                                           userverzeichnis[i]["passwort"], i)

    snackautomat3.writedata({"Product": produkt_liste, "User": user_liste})


zuruecksetzten()

"""
von Christoph Gruender
27.02.2022
in dieser Version:
    json datei zum speichern, doctags
    und viele Leerzeilen für eine gute übersicht
"""
import base64
import hashlib
import json

import bcrypt
import jsonpickle


class Product:
    """
    Abbildung eines Produktes zum speichern in json
    """

    def __init__(self, name="name", amount="amount", price="price", index=-1):
        """

        :param name:
        :param amount:
        :param price:
        :param index:
        """
        print("Create new Product: ", name)
        self.name = name
        if index == -1:
            self.index = len(readdata()["Product"])
        self.amount = amount
        self.price = price

    def reduce_amount(self):
        """
        :return:
        """
        self.amount -= 1

    def update_index(self):
        """
        :return:
        """
        self.index = len(readdata()["Product"])


def gen_hash_pw(password: str):
    """

    :param password: das zu dechiffrierende passwort
    :return: hash des pw
    """
    password = base64.b64encode(hashlib.sha256(password.encode("utf-8")).digest())
    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt(5)
    )
    #print("Salt:"+str(bcrypt.gensalt()))
    return hashed.decode()


def check_password(password: str, hashed: str):
    """
    :param hashed:
    :param password:
    :return: boolean ob das passwort und der hash zusammengehören
    """
    password = base64.b64encode(hashlib.sha256(password.encode("utf-8")).digest())
    hashed = hashed.encode("utf-8")
    return bcrypt.checkpw(password, hashed)


class User:
    """
    Abbildung eines Users zum speichern in json
    """

    def __init__(self, username="username", password="password", index=-1):
        print("Create new User: ", username)
        self.username = username
        self.balance = 0
        self.password = gen_hash_pw(password)
        if index == -1:
            self.index = len(readdata()["User"])

    def setbalance(self, balance):
        """
        :param balance:
        :return: None
        """
        print(f"Das neue Guthaben beträgt {balance}€")
        self.balance = balance

    def update_index(self):
        """
        :return:
        """
        self.index = len(readdata()["User"])


def writedata(data):
    """
    :param data: Sollte im schema [Automatenbelegung, userdaten] übergeben werden
    :return: nix
    """
    frozen = jsonpickle.encode(data)
    with open('snackdaten3.json', 'w', encoding="utf-8") as outfile:
        json.dump(frozen, outfile)


def readdata() -> dict:
    """
    :return: returnt Daten der json Datei 'Snackdaten.json'
    """
    try:
        with open('snackdaten3.json', encoding="utf-8") as infile:
            jsondata = json.load(infile)
        thawed = jsonpickle.decode(jsondata)
        return thawed
    except FileNotFoundError:
        print("Json file konnte nicht gefunden werden")
        return {}


def analyzeinput(key, aktuellerstatus, usernumber) -> int:
    """

    :param usernumber: Der index des den Automaten angemeldeten Kundens
    :param key: Die zu analysierende Eingabe
    :param aktuellerstatus: Der aktuelle Status des Systems
    :return: Der Status in den das System, je nach Eingabe gesetzt werden soll
    """
    if key in "L" or key in "l":
        returner = 0

    elif key in "E" or key in "e":
        returner = 1

    elif key in "W" or key in "w":
        returner = 2

    elif key in "A" or key in "a":
        returner = 6

    elif key in "K" or key in "k":
        balance = readdata()["User"][str(usernumber)].balance
        print("Ihr aktueller balance beträgt " + str(balance) + "€")
        returner = aktuellerstatus

    else:
        print("\n\nLeider konnten wir ihre Eingabe nicht verstehen."
              "\nBitte versuchen Sie es erneut.")
        returner = aktuellerstatus

    return returner


def produktwaehlen(usernumber) -> (int, int):
    """
    :param usernumber:  Der index des den Automaten angemeldeten Kundens
    :return: Der Index des gekauften Produktes und der neue Status im Format (index, status)
    """

    angebot: dict = readdata()["Product"]
    for i in range(1, len(angebot) + 1):
        angebot_i: Product = angebot[str(i)]
        if angebot_i.amount != 0:
            print(str(i), " : ", angebot_i.name, " ",
                  angebot_i.amount,
                  "stück verfügbar für ", angebot_i.price, " €")

    try:
        num = int(input("Welches Produkt möchten Sie wählen (1-10)?"))
    except ValueError:
        print("ungültige eingabe")
        num = -1

    if num < 1 or num > len(angebot):
        print("ungültige eingabe")
        return 0, 2

    try:
        produkt = readdata()["Product"].get(str(num))
        preis = float(produkt.price)
        anzahl = int(produkt.amount)
    except TypeError:
        print("Dieses Produkt haben wir leider nicht")
        return 0, 2

    if readdata()["User"][str(usernumber)].balance >= preis and anzahl > 0:
        status = 3
    else:
        status = 4
    return num, status


def produktkaufen(produktnr, usernr) -> {int, float}:
    """
    Produkt ist bezahlbar und wird gekauft
    :param usernr:  Der index des den Automaten angemeldeten Kundens
    :param produktnr: Der Index des zu kaufenden Produktes
    :return: Status für nächstes user interface, preis des gekauften Produktes
    """
    angebot = readdata()["Product"]
    product = angebot.get(str(produktnr))
    user = readdata()["User"]
    print("\n\n\nHier haben Sie ihren " + product.name + "\nVielen Dank für ihren Einkauf")
    user[str(usernr)].balance = user[str(usernr)].balance - product.price
    angebot[str(produktnr)].reduce_amount()
    writedata({"Product": angebot, "User": user})
    return 5, product.price


def nutzerhinzufuegen(username: str, password: str) -> int:
    """

    :param password:
    :param username: Den Namen für den neuen Nutzer
    :return: index:int des neuen Nutzers
    """
    index = len(readdata().get("User")) + 1
    nutzer = readdata()["User"]
    nutzer[index] = User(username, password)
    writedata(
        {"Product": readdata()["Product"], "User": nutzer})
    return index


def welcome():
    """

    :return: Der Index des Nutezrs und Status 5, der den Nutzer ins Hauptmenü sendet
    """
    # print(list(map(lambda c: f'{c}: {c.get("name")}', readdata().get("User"))))
    user = readdata()["User"]
    for i in range(1, len(user) + 1):
        userdieserschleife = user[str(i)]
        print(str(i), " : ", userdieserschleife.username)
    usernummer = input(
        "\n\n\nHerzlich Wilkommen am schnieken Snackautomaten\n"
        "Bitte geben Sie Ihre usernummer ein\n"
        "oder drücken sie <N/n> um einen neuen Nutzer anzulegen"
    )
    if "n" in usernummer or "N" in usernummer:
        nutzerhinzufuegen(input("Bitte geben Sie einen gewünschten Nutzernamen ein!"),
                          input("Bitte geben Sie ihr gewünschtes Passwort ein"))
        return -1, 0
    password = input("Bitte geben Sie ihr passwort ein")

    try:
        if check_password(password, readdata()["User"][usernummer].password):
            print("Hallo ", readdata()["User"][str(usernummer)].username)
        else:
            print("Wrong Password, please try again")
            return 0, 0
    except KeyError:
        print("\nWir konnten diesen Nutzer leider nicht finden")
        return 0, 0
    return usernummer, 5


def einzahlen(usernummer) -> int:
    """
    :param usernummer: Der index des den Automaten angemeldeten Kundens
    :return: Den Status des nächsten Userinterface
    """
    user: dict = readdata()["User"]
    try:
        neuerbetrag = user[str(usernummer)].balance + float(input("Wie viel möchten sie Einzahlen"))
        user[str(usernummer)].setbalance(neuerbetrag)
    except ValueError:
        print("Oops, das war keine Zahl")
        return 1
    writedata({"Product": readdata()["Product"], "User": user})
    analyzeinput("K", 1, usernummer)
    return 5


def checkjson(status: int):
    """

    :return: -1 wenn jsondaten nicht lesbar
    """
    try:
        if readdata() is None:
            print("FileNotFound")
            return -1
        var: dict = readdata()
        # Testzugriff
        if var["Product"]["1"].price is not None:
            return status
    except FileNotFoundError:
        print("FileError")
        return -1
    else:
        return status


def main() -> {}:
    """
    In der main funktion dieses Snackautomates wird ein nutzer wie in einem Automaten
    durch diskrete zustände des indizes "status" in die lage versetzt aus 10 Produkten einen
    :return: optimalerweise nichts, bei abbruch Fehlercode :(
    """

    status = usernummer = produktnummer = 0
    while status != -1:
        status = checkjson(status)
        if status == 0:
            usernummer, status = welcome()

        elif status == 1:
            status = einzahlen(usernummer)

        elif status == 2:
            produktnummer, status = produktwaehlen(usernummer)

        elif status == 3:
            status = produktkaufen(produktnummer, usernummer)

        elif status == 4:
            # Produkt ist zu teuer oder nicht mehr vorhanden --> wir nicht gekauft
            if readdata()["Product"][str(produktnummer)].amount == 0:
                print("\n\n\nOh nein, das Produkt ist ausverkauft.")
            else:
                print("\n\n\nOh nein, das Produkt ist zu teuer.")
            status = 5

        elif status == 5:
            print("\nDie balance beträgt ", str(readdata()["User"][str(usernummer)].balance), "€")
            key = input("\n\nUm Geld einzuzahlen drücken Sie <E/e>\n"
                        "Um ein Produkt zu wählen drücken Sie <W/w>\n"
                        "Um den balance anzuzeigen drücken Sie <K/k>\n"
                        "Zum Logout drücken Sie <L/l>"
                        "Um den Kaufvorgang abzubrechen drücken Sie <A/a>")
            status = analyzeinput(key, status, usernummer)

        elif status == 6:
            print("Vergessen Sie nicht wiederzukommen, und ihr Restguthaben in Höhe von "
                  + str(readdata()["User"][usernummer].balance) +
                  "€ in leckere Snacks zu investieren."
                  "\nEinen Schönen tag noch und bis nächstes Mal")
            status = -1

        else:
            if status != -1:
                status = 0


if __name__ == "__main__":
    main()

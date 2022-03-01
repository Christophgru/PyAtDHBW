import sys

nutzerDatenArray = [["test", "123", 0]]
nutzerID = -1


def getNutzerdaten(typ):
    if typ == -1:
        return nutzerDatenArray[nutzerID]
    return nutzerDatenArray[nutzerID][typ]



def durchsucheDatenbank(suchbegriff, type):
    for i in range(0, len(nutzerDatenArray)):
        if nutzerDatenArray[int(i)][int(type)] == suchbegriff:
            return i
    return -1
def setkontostand(zahl):
    nutzerDatenArray[nutzerID][2]=zahl


while True:
    eingabeuser = input("Insert Username")
    nutzerID = durchsucheDatenbank(eingabeuser, 0)
    if nutzerID != -1:
        eingabepw = input("Insert Password")
        if nutzerDatenArray[nutzerID][1] == eingabepw:
            nutzer = eingabeuser
        else:
            print("Wrong Password, please try again with a different one")
            nutzerID=-1
    else:
        Uname = input("User could not be Found. Insert new Username to create new account")
        pwd = input("Insert Passwort")
        newUser = [Uname, pwd, 0]
        nutzerDatenArray.append(newUser)
        print("Ein neuer Nutzer wurde erstellt, bitte melden Sie sich jetzt an")
    kontostand=getNutzerdaten(2)
    while nutzerID != -1:
        eingabe = input("Hallo " + nutzerDatenArray[nutzerID][0] + " Was möchten Sie machen? \nE für Einzahlung\nA für Auszahlung\nK für Kontostand\nB für Beenden\nS für Shutdown")
        if (eingabe == "E") | (eingabe == "e"):
            einzahlen = int(input("Wie viel möchten Sie Einzahlen?"))
            setkontostand(kontostand+einzahlen)
            kontostand=getNutzerdaten(2)
            print("Ihr neuer Kontostand ist ", kontostand, "€")
        elif (eingabe == "A") | (eingabe == "a"):
            auszahlen = int(input("Wie viel möchten Sie auszahelen?"))
            if auszahlen > kontostand:
                print("Ihr Konto ist nicht genügend gedeckt :(")
            else:
                setkontostand(kontostand-auszahlen)
                kontostand = getNutzerdaten(2)
                print("Ihr neuer Kontostand ist ", kontostand, "€")
        elif (eingabe == "B") | (eingabe == "b"):
            nutzerID = -1
            kontostand=0
            nutzer = ""
        elif (eingabe == "S") | (eingabe == "S"):
            sys.exit()
        elif (eingabe == "K") | (eingabe == "k"):
            print("Ihr Kontostand beträgt ", kontostand, "€")
        else:
            print("Diesen Befehl konnte leider nicht ausgeführt werden")

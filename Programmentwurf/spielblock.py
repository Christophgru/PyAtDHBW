import json
import jsonpickle


class Spielblock:
    indexlist = ["Einser","Zweier","Dreier","Vierer","Funfer","Sechser","Oben","Bonus","GesamtOben",
                 "Dreierpasch","Viererpasch","Full-House","Kleine-Straße","Große-Straße","Kniffel",
                 "Chance","Unten","Oben","Gesamt"]

    def __init__(self):
        liste = [{"1": {"Einser": [0, 0]}}, {"2": {"Zweier": [0, 0]}}, {"3": {"Dreier": [0, 0]}},
                 {"4": {"Vierer": [0, 0]}},
                 {"5": {"Funfer": [0, 0]}}, {"6": {"Sechser": [0, 0]}}, {"7": {"Oben": [0, 0]}},
                 {"8": {"Bonus": [0, 0]}},
                 {"9": {"GesamtOben": [0, 0]}}, {"10": {"Dreierpasch": [0, 0]}}, {"11": {"Viererpasch": [0, 0]}},
                 {"12": {"Full-House": [0, 0]}},
                 {"13": {"Kleine-Straße": [0, 0]}}, {"14": {"Große-Straße": [0, 0]}}, {"15": {"Kniffel": [0, 0]}},
                 {"16": {"Chance": [0, 0]}},
                 {"17": {"Unten": [0, 0]}}, {"18": {"Oben": [0, 0]}}, {"19": {"Gesamt": [0, 0]}}]
        self.freeze(liste)

    def freeze(self, item):
        with open("Block.json", "w") as freezer:
            frozen_list = jsonpickle.encode(item)
            json.dump(frozen_list, freezer)

    def thaw(self):
        with open("Block.json") as heater:
            frozen_list = json.load(heater)
            thawed_list = jsonpickle.decode(frozen_list)
            return thawed_list

    def punkteeinlesen(self, row, player, *value):
        block = self.thaw()
        column = block[row - 1]
        category = column[str(row)]
        shelf = category[self.indexlist[row-1]]
        calc_sum = 0
        if row <= 5:
            for number in value:
                if number == row-1:
                    calc_sum += number
            shelf[player] = calc_sum
        if row == 9 or row == 10 or row == 15:
            for number in value:
                calc_sum += number
            shelf[player] = calc_sum
        if row == 11:
            shelf[player] = 25
        if row == 12:
            shelf[player] = 30
        if row == 13:
            shelf[player] = 40
        if row == 14:
            shelf[player] = 50
        self.freeze(block)

    def ausgabe(self):
        trie = self.thaw()
        for i in range(trie.__len__()):
            print(trie[i])

    def valuing(self, player):
        plan = self.thaw()
        column = plan[6]
        category = column["5"]
        shelf = category[self.indexlist[5]]

    def allezeilenvoll(self):
        x = liste.__getitem__(18).get("19").get("Gesamt")
        x1 = x.__getitem__(0)
        x2 = x.__getitem__(1)
        if x1 == 0 or x2 == 0:
            return False
        else:
            return True

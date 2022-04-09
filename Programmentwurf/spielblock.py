# steve

import json
import jsonpickle

liste = [{"1": {"Einser": [0, 0]}}, {"2": {"Zweier": [0, 0]}},{"3": {"Dreier": [0, 0]}},{"4": {"Vierer": [0, 0]}},
        {"5": {"Funfer": [0, 0]}},{"6": {"Sechser": [0, 0]}},{"7": {"Oben": [0, 0]}},{"8": {"Bonus": [0, 0]}},
        {"9": {"GesamtOben": [0, 0]}},{"10": {"Dreierpasch": [0, 0]}},{"11": {"Viererpasch": [0, 0]}},{"12": {"Full-House": [0, 0]}},
        {"13": {"Kleine-Straße": [0, 0]}},{"14": {"Große-Straße": [0, 0]}},{"15": {"Kniffel": [0, 0]}},{"16": {"Chance": [0, 0]}},
        {"17": {"Unten": [0, 0]}},{"18": {"Oben": [0, 0]}},{"19": {"Gesamt": [0, 0]}}]


class Spielblock:

    indexlist = ["Einser","Zweier","Dreier","Vierer","Funfer","Sechser","Oben","Bonus","GesamtOben",
                 "Dreierpasch","Viererpasch","Full-House","Kleine-Straße","Große-Straße","Kniffel",
                 "Chance","Unten","Oben","Gesamt"]

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
        print(block)
        column = block[row - 1]
        print(column)
        category = column[str(row)]
        shelf = category[self.indexlist[row-1]]
        if row <= 6:
            calc_sum = 0
            for number in value:
                calc_sum += number
            shelf[player] = calc_sum
        self.freeze(block)

    def ausgabe(self):
        trie = self.thaw()
        for i in range(trie.__len__()):
            print(trie[i])

"""
@todo Steve bitte Docstrings ausfüllen/Vorschlag für too many branches in L:71 & => switch case
@todo/too many branches&statements in 149 muss selbst lösen XD
"""

import json
import string

import jsonpickle
from prettytable import PrettyTable


class Spielblock:
    """

    """
    indexlist = ["Einser", "Zweier", "Dreier", "Vierer", "Funfer",
                 "Sechser", "Oben", "Bonus", "GesamtOben",
                 "Dreierpasch", "Viererpasch", "Full-House", "Kleine-Straße", "Große-Straße", "Kniffel",
                 "Chance", "Unten", "Oben", "Gesamt"]

    first_line = [[0 for x in range(2)] for y in range(6)]
    second_line = [[0 for z in range(2)] for k in range(7)]
    for i in range(6):
        for y in range(2):
            first_line[i][y] = False
    for i in range(7):
        for y in range(2):
            second_line[i][y] = False
    oben = [False, False]
    unten = [False, False]
    ende = [False, False]
    endstand = [0, 0]

    def __init__(self):
        liste = [{"1": {"Einser": ['-', '-']}}, {"2": {"Zweier": [None, None]}},
                 {"3": {"Dreier": [None, None]}}, {"4": {"Vierer": [None, None]}},
                 {"5": {"Funfer": [None, None]}}, {"6": {"Sechser": [None, None]}},
                 {"7": {"Oben": [None, None]}}, {"8": {"Bonus": [None, None]}},
                 {"9": {"GesamtOben": [None, None]}}, {"10": {"Dreierpasch": [None, None]}},
                 {"11": {"Viererpasch": [None, None]}}, {"12": {"Full-House": [None, None]}},
                 {"13": {"Kleine-Straße": [None, None]}}, {"14": {"Große-Straße": [None, None]}},
                 {"15": {"Kniffel": [None, None]}}, {"16": {"Chance": [None, None]}},
                 {"17": {"Unten": [None, None]}}, {"18": {"Oben": [None, None]}},
                 {"19": {"Gesamt": [None, None]}}]

        self.freeze(liste)

    @classmethod
    def freeze(cls, item):
        """

        @param item: Objekt der Klasse Spielblock:
        @type item: Spielblock:
        @return: -
        @rtype: -
        """

        with open("Block.json", "w", encoding="utf-8") as freezer:
            frozen_list = jsonpickle.encode(item)
            json.dump(frozen_list, freezer)

    @classmethod
    def thaw(cls):
        """

        @return: json Spielblock object
        @rtype: Spielblock
        """
        with open("Block.json", encoding="utf-8") as heater:
            frozen_list = json.load(heater)
            thawed_list = jsonpickle.decode(frozen_list)
            return thawed_list

    def punkteeinlesen(self, row, player, leer, *value):
        """

        @param leer: bool if row already has a value in it
        @param row: the row you want to enter your value
        @type row: int
        @param player: 0= if it's player 1's turn 1 if it's player 2's turn
        @type player: int
        @param value: number of the dices
        @type value: int
        @return: nothing
        @rtype: nothing
        """

        block = self.thaw()
        column = block[row - 1]
        category = column[str(row)]
        shelf = category[self.indexlist[row - 1]]
        calc_sum = 0
        match row:
            case 12:
                if leer:
                    shelf[player] = 0
                else:
                    shelf[player] = 25
            case 13:
                if leer:
                    shelf[player] = 0
                else:
                    shelf[player] = 30
            case 14:
                if leer:
                    shelf[player] = 0
                else:
                    shelf[player] = 40
            case 15:
                if leer:
                    shelf[player] = 0
                else:
                    shelf[player] = 50
            case _:
                if row in (10, 11, 16):
                    for number in value:
                        calc_sum += number
                    if leer:
                        shelf[player] = 0
                    else:
                        shelf[player] = calc_sum
        if row <= 6:
            for number in value:
                if number == row:
                    calc_sum += number
            shelf[player] = calc_sum
            self.first_line[row - 1][player] = True
        else:
            self.second_line[row - 10][player] = True
        self.freeze(block)
        self.valuing(player)

    def ausgabe(self, name1: string, name2: string):
        """
        Method to prrint the entire Spielblock
        @return: nothing
        @rtype: nothing
        """
        trie = self.thaw()
        t = PrettyTable(['Zeile', 'Kniffel©', name1, name2])
        for i in range(trie.__len__()):
            zeile = trie[i]
            zwischen2 = zeile[str(i + 1)]
            zwischen3 = zwischen2[self.indexlist[i]]
            t.add_row([str(i + 1), self.indexlist[i], zwischen3[0], zwischen3[1]])
        print(t)

    def addoben(self, player, calc_sum, folder):
        """

        @param player: same as in punkteeinlesen(), indicates the player who's playing right now
        @type player: int
        @param calc_sum: int to calculate the values of the rows
        @param folder: the thawed obkect from json
        @type folder: Spielblock
        """
        for i in range(1, 7):
            column = folder[i - 1]
            category = column[str(i)]
            shelf = category[self.indexlist[i - 1]]
            calc_sum += shelf[player]
        column = folder[6]
        category = column[str(7)]
        shelf = category[self.indexlist[6]]
        shelf[player] = calc_sum
        self.freeze(folder)
        if calc_sum >= 63:
            folder = self.thaw()
            column = folder[7]
            category = column[str(8)]
            shelf = category[self.indexlist[7]]
            shelf[player] = 35
            self.freeze(folder)
            folder = self.thaw()
            column = folder[8]
            category = column[str(9)]
            shelf = category[self.indexlist[8]]
            shelf[player] = calc_sum + 35
            column = folder[17]
            category = column[str(18)]
            shelf = category[self.indexlist[17]]
            shelf[player] = calc_sum + 35
            self.oben[player] = True
            self.freeze(folder)
        else:
            folder = self.thaw()
            column = folder[8]
            category = column[str(9)]
            shelf = category[self.indexlist[8]]
            shelf[player] = calc_sum
            column = folder[17]
            category = column[str(18)]
            shelf = category[self.indexlist[17]]
            shelf[player] = calc_sum
            self.oben[player] = True
            self.freeze(folder)

    def addunten(self, player, calc_sum, folder):
        """

        @param player: same as in punkteeinlesen(), indicates the player who's playing right now
        @type player: int
        @param calc_sum: int to calculate the values of the rows
        @param folder: the thawed obkect from json
        @type folder: Spielblock
        """
        for i in range(10, 17):
            column = folder[i - 1]
            category = column[str(i)]
            shelf = category[self.indexlist[i - 1]]
            calc_sum += shelf[player]
        column = folder[16]
        category = column[str(17)]
        shelf = category[self.indexlist[16]]
        shelf[player] = calc_sum
        self.unten[player] = True
        self.freeze(folder)

    def valuing(self, player):
        """

        @param player: same as in punkteeinlesen(), indicates the player who's playing right now
        @type player: int
        @return: if the game is over returns gameover
        @rtype: bool
        """
        folder = self.thaw()
        calcoben1 = 0
        calcoben2 = 0
        calcunten1 = 0
        calcunten2 = 0
        calc_sum = 0
        for i in range(6):
            if self.first_line[i][player]:
                if player == 0:
                    calcoben1 += 1
                else:
                    calcoben2 += 1

        for i in range(7):
            if self.second_line[i][player]:
                if player == 0:
                    calcunten1 += 1
                else:
                    calcunten2 += 1
        if calcoben1 == 6 or calcoben2 == 6:
            self.addoben(player, calc_sum, folder)
        if calcunten1 == 7 or calcunten2 == 7:
            self.addunten(player, calc_sum, folder)
        if self.unten[player] and self.oben[player]:
            folder = self.thaw()
            column = folder[16]
            category = column[str(17)]
            shelf = category[self.indexlist[16]]
            calc1 = shelf[player]
            column = folder[17]
            category = column[str(18)]
            shelf = category[self.indexlist[17]]
            calc2 = shelf[player]
            column = folder[18]
            category = column[str(19)]
            shelf = category[self.indexlist[18]]
            shelf[player] = calc1 + calc2
            self.endstand[player] = calc1 + calc2
            self.ende[player] = True
            self.freeze(folder)

    def gamened(self):
        """

        @return: the final values of each player
        @rtype: int
        """
        return self.ende[0] and self.ende[1]

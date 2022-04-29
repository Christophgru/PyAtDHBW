"""
gameblock-class-file
"""

import json
import string

import jsonpickle
from prettytable import PrettyTable


class Gameblock:
    """

    Class for calculating and entering values of the dice game Kniffel

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
        liste = [{"1": {"Einser": ['-', '-']}}, {"2": {"Zweier": ['-', '-']}},
                 {"3": {"Dreier": ['-', '-']}}, {"4": {"Vierer": ['-', '-']}},
                 {"5": {"Funfer": ['-', '-']}}, {"6": {"Sechser": ['-', '-']}},
                 {"7": {"Oben": ['-', '-']}}, {"8": {"Bonus": ['-', '-']}},
                 {"9": {"GesamtOben": ['-', '-']}}, {"10": {"Dreierpasch": ['-', '-']}},
                 {"11": {"Viererpasch": ['-', '-']}}, {"12": {"Full-House": ['-', '-']}},
                 {"13": {"Kleine-Straße": ['-', '-']}}, {"14": {"Große-Straße": ['-', '-']}},
                 {"15": {"Kniffel": ['-', '-']}}, {"16": {"Chance": ['-', '-']}},
                 {"17": {"Unten": ['-', '-']}}, {"18": {"Oben": ['-', '-']}},
                 {"19": {"Gesamt": ['-', '-']}}]

        self.freeze(liste)

    @classmethod
    def freeze(cls, item):
        """

        @param item: Objekt der Klasse Gameblock:
        @type item: Gameblock:
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
        @rtype: Gameblock
        """
        with open("Block.json", encoding="utf-8") as heater:
            frozen_list = json.load(heater)
            thawed_list = jsonpickle.decode(frozen_list)
            return thawed_list

    def inputpoints(self, row, player, empty, *value):
        """

        @param empty: bool if row already has a value in it
        @param row: the row you want to enter your value
        @type row: int
        @param player: 0= if it's player 1's turn 1 if it's player 2's turn
        @type player: int
        @param value: number of the dices
        @type value: int
        @return: nothing
        @rtype: nothing
        """
        possible_values = {12: 25, 13: 30, 14: 40, 15: 50}
        block = self.thaw()
        column = block[row - 1]
        category = column[str(row)]
        shelf = category[self.indexlist[row - 1]]
        calc_sum = 0
        if empty:
            possible_values[row] = 0
        match row:
            case 12:
                shelf[player] = possible_values[row]
            case 13:
                shelf[player] = possible_values[row]
            case 14:
                shelf[player] = possible_values[row]
            case 15:
                shelf[player] = possible_values[row]
            case _:
                if row in (10, 11, 16):
                    for number in value:
                        calc_sum += number
                    if empty:
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

    def output(self, name1: string, name2: string, *diceeyes):
        """
        Method to print the entire Gameblock
        @return: nothing
        @rtype: nothing
        """
        trie = self.thaw()
        _table = PrettyTable(['Zeile', 'Kniffel©', name1, name2])
        for i in range(19):
            zeile = trie[i]
            zwischen2 = zeile[str(i + 1)]
            zwischen3 = zwischen2[self.indexlist[i]]
            _table.add_row([str(i + 1), self.indexlist[i], zwischen3[0], zwischen3[1]])
        print(_table)
        try:
            print("Würfel:" + str(diceeyes[0]) + " " + str(diceeyes[1]) + " " + str(diceeyes[2])
                  + " " + str(diceeyes[3]) + " " + str(diceeyes[4]))
        except IndexError:
            print("Game Vorbei")

    def addoben(self, player, calc_sum, folder):
        """

        @param player: same as in inputpoints(), indicates the player who's playing right now
        @type player: int
        @param calc_sum: int to calculate the values of the rows
        @param folder: the thawed object from json
        @type folder: Gameblock
        """
        for i in range(1, 7):
            column = folder[i - 1]
            category = column[str(i)]
            shelf = category[self.indexlist[i - 1]]
            wert = shelf[player]
            try:
                calc_sum += int(wert)
            except ValueError:
                calc_sum += 0
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

        @param player: same as in inputpoints(), indicates the player who's playing right now
        @type player: int
        @param calc_sum: int to calculate the values of the rows
        @param folder: the thawed obkect from json
        @type folder: Gameblock
        """
        for i in range(10, 17):
            column = folder[i - 1]
            category = column[str(i)]
            shelf = category[self.indexlist[i - 1]]
            wert = shelf[player]
            try:
                calc_sum += int(wert)
            except ValueError:
                calc_sum += 0
        column = folder[16]
        category = column[str(17)]
        shelf = category[self.indexlist[16]]
        shelf[player] = calc_sum
        self.unten[player] = True
        self.freeze(folder)

    def valuing(self, player):
        """

        @param player: same as in inputpoints(), indicates the player who's playing right now
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
            calc1: int = shelf[player]
            column = folder[17]
            category = column[str(18)]
            shelf = category[self.indexlist[17]]
            calc2: int = shelf[player]
            column = folder[18]
            category = column[str(19)]
            shelf = category[self.indexlist[18]]
            try:
                shelf[player] = calc1 + calc2
                self.endstand[player] = calc1 + calc2
            except TypeError:
                shelf[player] = 0
                self.endstand[player] = 0
            self.ende[player] = True
            self.freeze(folder)

    def gamened(self):
        """

        @return: bool whether the game is over or not
        @rtype: bool
        """
        return self.ende[0] and self.ende[1]

    def pluskniffel(self, playernumber: int):

        block = self.thaw()
        column = block[14]
        category = column[str(15)]
        shelf = category[self.indexlist[14]]
        shelf[playernumber] += 50



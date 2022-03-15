# pylint: diable=C
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from ProjectfilesSnackautomat3 import snackautomat3

wegzurjson = "ProjectfilesSnackautomat3/"


class TestSnackautomat3(TestCase):
    def test_check_pw(self):
        daten = snackautomat3.readdata(wegzurjson)
        pw_hash = daten["User"]['1']["password"]
        self.assertTrue(snackautomat3.check_password("hello", pw_hash))

    def test_check_analyseinput(self):
        inputs: list = ["l", "e", "w", "a", "k"]
        expected_outputs: list = [0, 1, 2, 6, 0]
        for i in range(0, 4):
            daten = snackautomat3.analyzeinput(inputs[i], 0, 0, wegzurjson)
            self.assertEqual(daten, expected_outputs[i])

    def test_anmelden(self):
        username = "1"
        password = "hello"
        erwartetet_ausgabe = ""
        # uitest
        # snackautomat3.welcome(wegzurjson)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("1\nhello")) as fake_in:
                snackautomat3.welcome(wegzurjson)
                fake_out.seek(199)
                self.assertIn("Hallo  Christoph\n", fake_out.read(20))

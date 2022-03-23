# pylint: diable=C
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from ProjectfilesSnackautomat3 import snackautomat3


class TestSnackautomat3(TestCase):
    def test_check_pw(self):
        daten = snackautomat3.readdata()
        pw_hash = daten["User"]['1']["password"]
        self.assertTrue(snackautomat3.check_password("hello", pw_hash))

    def test_check_analyseinput(self):
        inputs: list = ["l", "e", "w", "a", "k"]
        expected_outputs: list = [0, 1, 2, 6, 0]
        for i in range(0, 5):
            daten = snackautomat3.analyzeinput(inputs[i], 0, 1)
            self.assertEqual(daten, expected_outputs[i])

    def test_anmelden(self):
        username = "1"
        password = "hello"
        erwartetet_ausgabe = ""
        # uitest
        # snackautomat3.welcome(wegzurjson)
        inputstring = "1\nhello\ne\n10\nw\n1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                snackautomat3.welcome()
                fake_out.seek(199)
                if "Wrong Password" in fake_out.read(20):
                    raise AssertionError
                fake_out.seek(199)
                self.assertIn("Hallo  Christoph\n", fake_out.read(20))

    def test_Product_init(self):
        testprod = snackautomat3.Product("produkt", "20", "10")
        self.assertEqual(testprod.price, "10")
        testprod.reduce_amount()
        self.assertEqual(testprod.amount, "19")

    def test_produkr_waehlen(self):
        inputstring = "3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(inputstring)) as fake_in:
                snackautomat3.produktwaehlen(1)
                fake_out.seek(0)
                self.assertIn("Welches Produkt möchten Sie wählen", fake_out.read(800))

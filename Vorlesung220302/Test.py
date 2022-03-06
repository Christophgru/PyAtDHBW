# pylint: diable=C
from unittest import TestCase

from ProjectfilesSnackautomat3 import snackautomat3


class TestSnackautomat3(TestCase):
    def test_checkpw(self):
        daten = snackautomat3.readdata("ProjectfilesSnackautomat3/")
        pw_hash = daten["User"]['1']["password"]
        self.assertTrue(snackautomat3.check_password("hello", pw_hash))

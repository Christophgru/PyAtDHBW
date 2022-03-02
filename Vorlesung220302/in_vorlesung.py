# testen:
# falsche werte, falsche einheiten, funktionen überprüfen
import unittest
from io import StringIO
from unittest.mock import patch

from ProjectfilesSnackautomat3 import snackautomat3


class SnackAutomatTest(unittest.TestCase):
    def set_up(self):
        self.snacktomat = snackautomat3

    def test_anmelden(self):
        username = ""
        password = ""
        erwartetet_ausgabe = ""
        self.snacktomat.anmelden(username, password)
        # uitest
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.snacktomat.anmelden(username, password)
            self.asserEqual(fake_out.getvalue(), erwartetet_ausgabe)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO("absd\nasdj")) as fake_out:
                self.snacktomat.welcome()
                fake_out.seek(0)



# Propertys

class Test:
    def __init__(self):
        self.__my_var: int = 0

    # jetzt als .myvar aufrufbar
    @property
    def my_var(self):
        return self.__my_var

    @my_var.setter
    def my_var(self, new_value):
        if not isinstance(new_value, int):
            raise NotImplemented
        self.__my_var = new_value

    """
    Nicht so schön
    
    def get_my_var(self):
        return self.__my_var

    def set_my_var(self,new_value):
        if not isinstance(new_value,int):
            raise NotImplemented
        self.__my_var=new_value
        """


test = Test()
test.my_var = 1
print(test.my_var)

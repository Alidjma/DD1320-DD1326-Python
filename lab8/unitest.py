import unittest
from main import check_molecule

class TestSyntaxChecker(unittest.TestCase):

    def test_molecule(self):
        self.assertEqual(check_molecule("N"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Au"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("H2"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("P21"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Ag3"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Fe12"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Xx5"), "Formeln är syntaktiskt korrekt")

    def test_invalid_molecules(self):
        self.assertEqual(check_molecule("oa"), "Saknad stor bokstav vid radslutet oa")
        self.assertEqual(check_molecule("cr12"), "Saknad stor bokstav vid radslutet cr12")
        self.assertEqual(check_molecule("8"), "Saknad stor bokstav vid radslutet 8")
        self.assertEqual(check_molecule("Cr0"), "För litet tal vid radslutet")
        self.assertEqual(check_molecule("Pb1"), "För litet tal vid radslutet")
        self.assertEqual(check_molecule("H01011"), "För litet tal vid radslutet 1011")
        self.assertEqual(check_molecule("K01"), "För litet tal vid radslutet 1")

if __name__ == '__main__':
    unittest.main()

import unittest
from main import *


class TestMoleculeChecker(unittest.TestCase):

    def test_correct_molecules(self):
        self.assertEqual(check_molecule("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("H2O"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_molecule("Na332"), "Formeln är syntaktiskt korrekt")

    def test_incorrect_molecules(self):
        self.assertEqual(check_molecule("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
        self.assertEqual(check_molecule("C(OH4)C"), "Saknad siffra vid radslutet C")
        self.assertEqual(check_molecule("C(OH4C"), "Saknad högerparentes vid radslutet")
        self.assertEqual(check_molecule("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
        self.assertEqual(check_molecule("H0"), "För litet tal vid radslutet ")
        self.assertEqual(check_molecule("H1C"), "För litet tal vid radslutet C")
        self.assertEqual(check_molecule("H02C"), "För litet tal vid radslutet 2C")
        self.assertEqual(check_molecule("Nacl"), "Saknad stor bokstav vid radslutet cl")
        self.assertEqual(check_molecule("a"), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(check_molecule("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(check_molecule(")"), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(check_molecule("2"), "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()

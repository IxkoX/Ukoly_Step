# 15_get_upper_chars.py

import unittest
import get_upper_chars as upper


class TestGetUpperChars(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(upper.get_upper_chars(""), "", "Prázdný řetězec by měl vrátit prázdný řetězec.")

    def test_no_uppercase(self):
        self.assertEqual(upper.get_upper_chars("ahoj"), "", "Řetězec bez velkých písmen by měl vrátit prázdný řetězec.")

    def test_only_uppercase(self):
        self.assertEqual(upper.get_upper_chars("ABC"), "ABC", "Řetězec pouze s velkými písmeny by měl vrátit totéž.")

    def test_mixed_case(self):
        self.assertEqual(upper.get_upper_chars("AhojSvěte"), "AS", "Smíšený řetězec by měl vrátit pouze velká písmena.")

    def test_with_numbers_and_symbols(self):
        self.assertEqual(upper.get_upper_chars("A1!Bc@D"), "ABD", "Číslice a symboly by měly být ignorovány.")

    def test_with_whitespace(self):
        self.assertEqual(upper.get_upper_chars("Ahoj jsem tady"), "A", "Mezery by neměly ovlivňovat výstup.")

if __name__ == '__main__':
    unittest.main()

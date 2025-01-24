# is_teenager_test.py

import unittest
from is_teenager import is_teenager

class TestIsTeenager(unittest.TestCase):
    
    def test_under_13(self):
        self.assertFalse(is_teenager(12), "Děti do 13 let nejsou teenageři.")

    def test_old_13(self):
        self.assertTrue(is_teenager(13), "13 let by mělo vrátit True.")

    def test_old_19(self):
        self.assertTrue(is_teenager(19), "19 let by mělo vrátit True.")

    def test_above_20(self):
        self.assertFalse(is_teenager(20), "20 let už není teenager.")

    def test_negative_age(self):
        self.assertFalse(is_teenager(-1), "Záporbý věk neexistuje - nejsi naživu")

    def test_zero_age(self):
        self.assertFalse(is_teenager(0), "0 let je novorozeně ne teenager.")

if __name__ == '__main__':
    unittest.main()
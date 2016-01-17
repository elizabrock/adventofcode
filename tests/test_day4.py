from unittest import TestCase
from day4 import Day4

class TestDay4(TestCase):
    def test_find_n_for_key_abcdef(self):
        input = 'abcdef'
        expected = 609043
        actual = Day4.find_n_for_key(input, 5)
        self.assertEqual(expected, actual)

    def test_find_n_for_key_pqrstuv(self):
        input = 'pqrstuv'
        expected = 1048970
        actual = Day4.find_n_for_key(input, 5)
        self.assertEqual(expected, actual)

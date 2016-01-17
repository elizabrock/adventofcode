from unittest import TestCase
from day5 import SantasList, Word1, Word2

class TestSantasList(TestCase):
    def test_word1_nice_item_count_empty(self):
        input = ''
        expected = 0
        actual = SantasList(Word1, input).nice_item_count()
        self.assertEqual(expected, actual)

    def test_word1_nice_item_count_short(self):
        input = 'ugknbfddgicrmopn\naaa\njchzalrnumimnmhp\nhaegwjzuvuyypxyu\naaa'
        expected = 3
        actual = SantasList(Word1, input).nice_item_count()
        self.assertEqual(expected, actual)

    def test_word2_nice_item_count_empty(self):
        input = ''
        expected = 0
        actual = SantasList(Word2, input).nice_item_count()
        self.assertEqual(expected, actual)

    def test_word2_nice_item_count_short(self):
        input = 'qjhvhtzxzqqjkmpb\nxxyxx\nuurcxstgmygtbstg\nieodomkazucvgmuy'
        expected = 2
        actual = SantasList(Word2, input).nice_item_count()
        self.assertEqual(expected, actual)
from unittest import TestCase
from day5 import SantasList

class TestSantasList(TestCase):
    def test_nice_item_count_empty(self):
        input = ''
        expected = 0
        actual = SantasList(input).nice_item_count()
        self.assertEqual(expected, actual)

    def test_nice_item_count_short(self):
        input = 'ugknbfddgicrmopn\naaa\njchzalrnumimnmhp\nhaegwjzuvuyypxyu\naaa'
        expected = 3
        actual = SantasList(input).nice_item_count()
        self.assertEqual(expected, actual)

from unittest import TestCase
from day6 import Santa

class TestSanta(TestCase):
    def test_coordinates_from_single_digit(self):
        santa = Santa()
        actual = santa._coordinates_from('turn on 0,0 through 0,0')
        expected = [0, 0, 0, 0]
        self.assertEqual(expected, actual)

    def test_coordinates_from_multiple_digit(self):
        santa = Santa()
        actual = santa._coordinates_from('toggle 900,100 through 999,555')
        expected = [900, 100, 999, 555]
        self.assertEqual(expected, actual)

    def test_send_instructions_on_one(self):
        santa = Santa()
        santa.send_instructions('turn on 0,0 through 0,0')
        self.assertEqual(1, santa._grid.lights_on_count())

    def test_send_instructions_on_all(self):
        santa = Santa()
        santa.send_instructions('turn on 0,0 through 999,999')
        self.assertEqual(1000000, santa._grid.lights_on_count())

    def test_send_instructions_toggle(self):
        santa = Santa()
        santa.send_instructions('toggle 0,0 through 999,0')
        self.assertEqual(1000, santa._grid.lights_on_count())
        santa.send_instructions('toggle 500,0 through 999,0')
        self.assertEqual(500, santa._grid.lights_on_count())

    def test_send_instructions_off(self):
        santa = Santa()
        santa.send_instructions('turn on 0,0 through 999,0')
        self.assertEqual(1000, santa._grid.lights_on_count())
        santa.send_instructions('turn off 0,0 through 499,0')
        self.assertEqual(500, santa._grid.lights_on_count())

    def test_send_instructions_multiple_lines(self):
        santa = Santa()
        santa.send_instructions('turn on 0,0 through 999,0\nturn off 0,0 through 499,0\ntoggle 999,999 through 999,999')
        self.assertEqual(501, santa._grid.lights_on_count())
from unittest import TestCase
from day3 import Traveler, Path

class TestTraveler(TestCase):
    def test_travel_0(self):
        path = Path()
        traveler = Traveler(path)
        self.assertEqual(1, len(path._locations_visited))

    def test_travel_1(self):
        path = Path()
        traveler = Traveler(path)
        traveler.travel('>')
        self.assertEqual(1, traveler._current_x)
        self.assertEqual(0, traveler._current_y)
        self.assertEqual(2, len(path._locations_visited))

    def test_houses_visited_single_visitor_4(self):
        path = Path()
        traveler = Traveler(path)
        traveler.travel('^')
        traveler.travel('>')
        traveler.travel('v')
        traveler.travel('<')
        self.assertEqual(0, traveler._current_x)
        self.assertEqual(0, traveler._current_y)
        self.assertEqual(4, len(path._locations_visited))
import unittest
from day3 import Router, Path, Traveler

class TestRouter(unittest.TestCase):

    def test_houses_visited_single_visitor_2(self):
        input = '>'
        expected = 2
        path = Path()
        Router.route(input, Traveler(path))
        self.assertEqual(expected, path.houses_visited())

    def test_houses_visited_single_visitor_4(self):
        input = '^>v<'
        expected = 4
        path = Path()
        Router.route(input, Traveler(path))
        self.assertEqual(expected, path.houses_visited())

    def test_houses_visited_long_single_visitor_2(self):
        input = '^v^v^v^v^v'
        expected = 2
        path = Path()
        Router.route(input, Traveler(path))
        self.assertEqual(expected, path.houses_visited())

    def test_houses_visited_multiple_visitors_2(self):
        input = '^v'
        expected = 3
        path = Path()
        Router.route(input, Traveler(path), Traveler(path))
        self.assertEqual(expected, path.houses_visited())

    def test_houses_visited_multiple_visitors_4(self):
        input = '^>v<'
        expected = 3
        path = Path()
        Router.route(input, Traveler(path), Traveler(path))
        self.assertEqual(expected, path.houses_visited())

    def test_houses_visited_long_multiple_visitors_2(self):
        input = '^v^v^v^v^v'
        expected = 11
        path = Path()
        Router.route(input, Traveler(path), Traveler(path))
        self.assertEqual(expected, path.houses_visited())

if __name__ == '__main__':
    unittest.main()

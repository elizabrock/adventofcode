import unittest
from day3 import TravelPath

class MyTestCase(unittest.TestCase):

    def test_houses_visited2(self):
        input = '>'
        expected = 2
        actual = TravelPath(input).houses_visited()
        self.assertEqual(expected, actual)

    def test_houses_visited4(self):
        input = '^>v<'
        expected = 4
        actual = TravelPath(input).houses_visited()
        self.assertEqual(expected, actual)

    def test_houses_visited_long2(self):
        input = '^v^v^v^v^v'
        expected = 2
        actual = TravelPath(input).houses_visited()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

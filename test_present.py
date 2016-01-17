from unittest import TestCase
from day2 import Present

class TestPresent(TestCase):
    def test_side_areas_zeros(self):
        expected = [0, 0, 0, 0, 0, 0]
        actual = Present(0, 0, 0).side_areas()
        self.assertEqual(expected, actual)

    def test_side_areas_rectangle1(self):
        expected = [6, 6, 12, 12, 8, 8]
        actual = Present(2, 3, 4).side_areas()
        self.assertEqual(expected, actual)

    def test_side_areas_rectangle2(self):
        expected = [1, 1, 10, 10, 10, 10]
        actual = Present(1, 1, 10).side_areas()
        self.assertEqual(expected, actual)

    def test_wrapping_paper_required_zeros(self):
        expected = 0
        actual = Present(0, 0, 0).wrapping_paper_required()
        self.assertEqual(expected, actual)

    def test_wrapping_paper_required_rectangle1(self):
        expected = 58
        actual = Present(2, 3, 4).wrapping_paper_required()
        self.assertEqual(expected, actual)

    def test_wrapping_paper_required_rectangle2(self):
        expected = 43
        actual = Present(1, 1, 10).wrapping_paper_required()
        self.assertEqual(expected, actual)

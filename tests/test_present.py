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

    def test_side_perimeters_zeros(self):
        expected = [0, 0, 0, 0, 0, 0]
        actual = Present(0, 0, 0).side_perimeters()
        self.assertEqual(expected, actual)

    def test_side_perimeters_rectangle1(self):
        expected = [10, 10, 14, 14, 12, 12]
        actual = Present(2, 3, 4).side_perimeters()
        self.assertEqual(expected, actual)

    def test_side_perimeters_rectangle2(self):
        expected = [4, 4, 22, 22, 22, 22]
        actual = Present(1, 1, 10).side_perimeters()
        self.assertEqual(expected, actual)

    def test_volume_zeros(self):
        expected = 0
        actual = Present(0, 0, 0).volume()
        self.assertEqual(expected, actual)

    def test_volume_rectangle1(self):
        expected = 24
        actual = Present(2, 3, 4).volume()
        self.assertEqual(expected, actual)

    def test_volume_rectangle2(self):
        expected = 10
        actual = Present(1, 1, 10).volume()
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


    def test_ribbon_paper_required_zeros(self):
        expected = 0
        actual = Present(0, 0, 0).ribbon_required()
        self.assertEqual(expected, actual)

    def test_ribbon_paper_required_rectangle1(self):
        expected = 34
        actual = Present(2, 3, 4).ribbon_required()
        self.assertEqual(expected, actual)

    def test_ribbon_paper_required_rectangle2(self):
        expected = 14
        actual = Present(1, 1, 10).ribbon_required()
        self.assertEqual(expected, actual)
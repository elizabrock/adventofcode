from unittest import TestCase
from day2 import PresentCollection

class TestPresentCollection(TestCase):
    def test_wrapping_paper_required(self):
        input = '2x3x4\n1x1x10'
        expected = 101
        actual = PresentCollection(input).wrapping_paper_required()
        self.assertEqual(expected, actual)

    def test_wrapping_paper_required_longer(self):
        input = '2x3x4\n1x1x10\n2x3x4\n1x1x10'
        expected = 202
        actual = PresentCollection(input).wrapping_paper_required()
        self.assertEqual(expected, actual)

    def test_count(self):
        input = '2x3x4\n1x1x10'
        expected = 2
        actual = len(PresentCollection(input)._presents)
        self.assertEqual(expected, actual)

    def test_count_longer(self):
        input = '2x3x4\n1x1x10\n2x3x4\n1x1x10'
        expected = 4
        actual = len(PresentCollection(input)._presents)
        self.assertEqual(expected, actual)
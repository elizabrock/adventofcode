from unittest import TestCase
from day5 import Word2

class TestWord2(TestCase):
    def test_is_nice_example_1(self):
        input = 'qjhvhtzxzqqjkmpb'
        self.assertTrue(Word2(input).is_nice())

    def test_is_nice_example_2(self):
        input = 'xxyxx'
        self.assertTrue(Word2(input).is_nice())

    def test_is_nice_example_3(self):
        input = 'uurcxstgmygtbstg'
        self.assertFalse(Word2(input).is_nice())

    def test_is_nice_example_4(self):
        input = 'ieodomkazucvgmuy'
        self.assertFalse(Word2(input).is_nice())

    def test_has_non_overlapping_letter_pair_1(self):
        input = 'xyxy'
        self.assertTrue(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_2(self):
        input = 'aabcdefgaa'
        self.assertTrue(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_3(self):
        input = 'aaa'
        self.assertFalse(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_4(self):
        input = 'qjhvhtzxzqqjkmpb'
        self.assertTrue(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_5(self):
        input = 'xxyxx'
        self.assertTrue(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_6(self):
        input = 'uurcxstgmygtbstg'
        self.assertTrue(Word2(input).has_non_overlapping_letter_pair())

    def test_has_non_overlapping_letter_pair_7(self):
        input = 'ieodomkazucvgmuy'
        self.assertFalse(Word2(input).has_non_overlapping_letter_pair())

    def test_has_oreo_pair_1(self):
        input = 'xyx'
        self.assertTrue(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_2(self):
        input = 'xyyx'
        self.assertFalse(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_3(self):
        input = 'abcdefeghi'
        self.assertTrue(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_4(self):
        input = 'aaa'
        self.assertTrue(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_5(self):
        input = 'aa'
        self.assertFalse(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_6(self):
        input = 'qjhvhtzxzqqjkmpb'
        self.assertTrue(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_7(self):
        input = 'xxyxx'
        self.assertTrue(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_8(self):
        input = 'uurcxstgmygtbstg'
        self.assertFalse(Word2(input).has_oreo_pair())

    def test_has_oreo_pair_9(self):
        input = 'ieodomkazucvgmuy'
        self.assertTrue(Word2(input).has_oreo_pair())
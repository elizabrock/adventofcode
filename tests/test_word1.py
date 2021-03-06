from unittest import TestCase
from day5 import Word1

class TestWord1(TestCase):
    def test_is_nice_with_only_vowels_no_double_letters(self):
        input = 'aeiou'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_with_vowels_and_double_letters(self):
        input = 'aaeiou'
        self.assertTrue(Word1(input).is_nice())

    def test_is_nice_with_double_letters_and_no_vowels(self):
        input = 'ddbbcc'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_does_like_aaa(self):
        input = 'aaa'
        self.assertTrue(Word1(input).is_nice())

    def test_is_nice_doesnt_like_ab(self):
        input = 'abaaa'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_doesnt_like_cd(self):
        input = 'cdaaa'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_doesnt_like_pq(self):
        input = 'pqaaa'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_doesnt_like_xy(self):
        input = 'xyaaa'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_example_1(self):
        input = 'ugknbfddgicrmopn'
        self.assertTrue(Word1(input).is_nice())

    def test_is_nice_example_2(self):
        input = 'aaa'
        self.assertTrue(Word1(input).is_nice())

    def test_is_nice_example_3(self):
        input = 'jchzalrnumimnmhp'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_example_4(self):
        input = 'haegwjzuvuyypxyu'
        self.assertFalse(Word1(input).is_nice())

    def test_is_nice_example_5(self):
        input = 'dvszwmarrgswjxmb'
        self.assertFalse(Word1(input).is_nice())

    def test_double_letters_empty(self):
        self.assertFalse(Word1("").has_double_letters())

    def test_double_letters_short(self):
        self.assertTrue(Word1("dd").has_double_letters())

    def test_double_letters_medium(self):
        self.assertTrue(Word1("ddc").has_double_letters())

    def test_double_letters_long(self):
        self.assertTrue(Word1("abcdd").has_double_letters())

    def test_double_letters_none(self):
        self.assertFalse(Word1("abcde").has_double_letters())


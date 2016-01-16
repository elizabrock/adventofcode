from unittest import TestCase
from day1 import Day1

class TestDay1(TestCase):
    def test_calculate1(self):
        expected = 0
        actual = Day1.calculate("(())")
        self.assertEqual(actual, expected)

    def test_calculate2(self):
        expected = 0
        actual = Day1.calculate("()()")
        self.assertEqual(actual, expected)

    def test_calculate3(self):
        expected = 3
        actual = Day1.calculate("(((")
        self.assertEqual(actual, expected)

    def test_calculate4(self):
        expected = 3
        actual = Day1.calculate("(()(()(")
        self.assertEqual(actual, expected)

    def test_calculate5(self):
        expected = 3
        actual = Day1.calculate("))(((((")
        self.assertEqual(actual, expected)

    def test_calculate6(self):
        expected = -1
        actual = Day1.calculate("())")
        self.assertEqual(actual, expected)

    def test_calculate7(self):
        expected = -1
        actual = Day1.calculate("))( ")
        self.assertEqual(actual, expected)

    def test_calculate8(self):
        expected = -3
        actual = Day1.calculate(")))")
        self.assertEqual(actual, expected)

    def test_calculate9(self):
        expected = -3
        actual = Day1.calculate(")())())")
        self.assertEqual(actual, expected)
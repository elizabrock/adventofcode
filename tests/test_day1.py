from unittest import TestCase
from day1 import Day1

class TestDay1(TestCase):
    def test_destination1(self):
        expected = 0
        actual = Day1("(())").destination()
        self.assertEqual(actual, expected)

    def test_destination2(self):
        expected = 0
        actual = Day1("()()").destination()
        self.assertEqual(actual, expected)

    def test_destination3(self):
        expected = 3
        actual = Day1("(((").destination()
        self.assertEqual(actual, expected)

    def test_destination4(self):
        expected = 3
        actual = Day1("(()(()(").destination()
        self.assertEqual(actual, expected)

    def test_destination5(self):
        expected = 3
        actual = Day1("))(((((").destination()
        self.assertEqual(actual, expected)

    def test_destination6(self):
        expected = -1
        actual = Day1("())").destination()
        self.assertEqual(actual, expected)

    def test_destination7(self):
        expected = -1
        actual = Day1("))( ").destination()
        self.assertEqual(actual, expected)

    def test_destination8(self):
        expected = -3
        actual = Day1(")))").destination()
        self.assertEqual(actual, expected)

    def test_destination9(self):
        expected = -3
        actual = Day1(")())())").destination()
        self.assertEqual(actual, expected)

    def test_enters_basement_at_1(self):
        expected = 1
        actual = Day1(")").enters_basement_at()
        self.assertEqual(actual, expected)

    def test_enters_basement_at_3(self):
        expected = 3
        actual = Day1("())").enters_basement_at()
        self.assertEqual(actual, expected)

    def test_enters_basement_at_5(self):
        expected = 5
        actual = Day1("()())").enters_basement_at()
        self.assertEqual(actual, expected)

    def test_enters_basement_never(self):
        expected = -1
        actual = Day1("()()").enters_basement_at()
        self.assertEqual(actual, expected)
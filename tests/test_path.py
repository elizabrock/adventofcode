from unittest import TestCase
from day3 import Path

class TestPath(TestCase):
    def test_mark_visit_to_increments_visits(self):
        path = Path()
        self.assertEqual(path._locations_visited[(1,1)], 0)
        path.mark_visit_to(1,1)
        self.assertEqual(path._locations_visited[(1,1)], 1)

    def test_houses_visited(self):
        path = Path()
        self.assertEqual(0, path.houses_visited())
        path.mark_visit_to(1,1)
        self.assertEqual(1, path.houses_visited())
        path.mark_visit_to(2,1)
        self.assertEqual(2, path.houses_visited())
        path.mark_visit_to(1,1)
        self.assertEqual(2, path.houses_visited())

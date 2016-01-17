from unittest import TestCase
from day6 import Grid

class TestGrid(TestCase):
    def test_lights_start_out_off(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())

    def test_toggle_one_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.toggle(0, 0, 0, 0)
        self.assertEqual(1, grid.lights_on_count())
        grid.toggle(0, 0, 0, 0)
        self.assertEqual(0, grid.lights_on_count())

    def test_toggle_multiple_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.toggle(0, 0, 4, 4)
        self.assertEqual(25, grid.lights_on_count())
        grid.toggle(0, 0, 2, 2)
        self.assertEqual(16, grid.lights_on_count())

    def test_turn_on_one_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.turn_on(0, 0, 0, 0)
        self.assertEqual(1, grid.lights_on_count())
        grid.turn_on(0, 0, 0, 0)
        self.assertEqual(1, grid.lights_on_count())

    def test_turn_on_multiple_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.turn_on(0, 0, 0, 0)
        self.assertEqual(1, grid.lights_on_count())
        grid.turn_on(0, 0, 4, 4)
        self.assertEqual(25, grid.lights_on_count())

    def test_turn_off_one_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.turn_on(0, 0, 0, 0)
        self.assertEqual(1, grid.lights_on_count())
        grid.turn_off(0, 0, 0, 0)
        self.assertEqual(0, grid.lights_on_count())
        grid.turn_off(0, 0, 0, 0)
        self.assertEqual(0, grid.lights_on_count())

    def test_turn_off_multiple_light(self):
        grid = Grid()
        self.assertEqual(0, grid.lights_on_count())
        grid.turn_on(0, 0, 4, 4)
        self.assertEqual(25, grid.lights_on_count())
        grid.turn_off(0, 0, 1, 1)
        self.assertEqual(21, grid.lights_on_count())
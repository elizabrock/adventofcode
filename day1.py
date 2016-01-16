import math

class Day1:
    def __init__(self, input):
        self._input = input

    def destination(self):
        return self._input.count("(") - self._input.count(")")

advent_code = open('day1_input.txt', 'r').read()
santa_floor = Day1(advent_code).destination()
print("Santa ends up on floor {0}.".format(santa_floor))
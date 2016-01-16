import math

class Day1:
    def __init__(self, input):
        self._input = input

    def destination(self):
        return self._input.count("(") - self._input.count(")")

    def enters_basement_at(self):
        floor = 0
        for i, char in enumerate(self._input):
            if char == "(":
                floor += 1
            else:
                floor -= 1
            if floor < 0:
                return i + 1
        return -1

advent_code = open('day1_input.txt', 'r').read()
santa_floor = Day1(advent_code).destination()
print("Santa ends up on floor {0}.".format(santa_floor))
basement_floor = Day1(advent_code).enters_basement_at()
print("Santa first entered the basement on floor {0}.".format(basement_floor))
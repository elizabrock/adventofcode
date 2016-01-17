from collections import defaultdict
import re

class Santa:
    def __init__(self):
        self._grid = Grid()

    def send_instructions(self, instructions):
        for instruction in instructions.splitlines():
            self._process_instruction(instruction)

    def _process_instruction(self, instruction):
        x1, y1, x2, y2 = self._coordinates_from(instruction)
        if instruction.startswith('turn on'):
            self._grid.turn_on(x1, y1, x2, y2)
        if instruction.startswith('turn off'):
            self._grid.turn_off(x1, y1, x2, y2)
        if instruction.startswith('toggle'):
            self._grid.toggle(x1, y1, x2, y2)

    def _coordinates_from(self, instruction):
        coordinates = re.match(r'[\w\s]* (\d+),(\d+) through (\d+),(\d+)', instruction).groups()
        return [int(coordinate) for coordinate in coordinates]

class Grid:
    def __init__(self):
        # All lights start out off
        self._grid = defaultdict(lambda: False)

    def toggle(self, x1, y1, x2, y2):
        self._iterate_over_range(lambda v: not v, x1, y1, x2, y2)

    def turn_on(self, x1, y1, x2, y2):
        self._iterate_over_range(lambda v: True, x1, y1, x2, y2)

    def turn_off(self, x1, y1, x2, y2):
        self._iterate_over_range(lambda v: False, x1, y1, x2, y2)

    def _iterate_over_range(self, func, x1, y1, x2, y2):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                pair = (x, y)
                self._grid[pair] = func(self._grid[pair])

    def lights_on_count(self):
        return list(self._grid.values()).count(True)

if __name__ == "__main__":
    instructions = open('input/day6_input.txt', 'r').read()
    santa = Santa()
    santa.send_instructions(instructions)
    print("After following Santa's instructions, there are {0} lights on.".format(santa._grid.lights_on_count()))
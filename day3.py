from collections import defaultdict

class TravelPath:

    def __init__(self, path):
        self._current_x = 0
        self._current_y = 0
        self._locations_visited = defaultdict(lambda: 0)
        self._locations_visited[(0,0)] = 1
        for direction in path:
            self.travel(direction)

    def houses_visited(self):
        return len(self._locations_visited)

    def travel(self, direction):
        # increment x and y
        # north (^), south (v), east (>), or west (<)
        if direction == '^':
            self._current_y += 1
        elif direction == 'v':
            self._current_y -= 1
        elif direction == '>':
            self._current_x += 1
        elif direction == '<':
            self._current_x -= 1
        # enter new location in hash
        self._locations_visited[(self._current_x, self._current_y)] += 1

if __name__ == "__main__":
    path = open('day3_input.txt', 'r').read()
    traveled_path = TravelPath(path)
    print("Santa will visit {0} houses.".format(traveled_path.houses_visited()))
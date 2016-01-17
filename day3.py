from collections import defaultdict

class Path:
    def __init__(self):
        self._locations_visited = defaultdict(lambda: 0)

    def mark_visit_to(self, x, y):
        self._locations_visited[(x, y)] += 1

    def houses_visited(self):
        return len(self._locations_visited)

class Traveler:
    def __init__(self, path):
        self._path = path;
        self._current_x = 0
        self._current_y = 0
        self.__send_location()

    def travel(self, direction):
        # north (^), south (v), east (>), or west (<)
        if direction == '^':
            self._current_y += 1
        elif direction == 'v':
            self._current_y -= 1
        elif direction == '>':
            self._current_x += 1
        elif direction == '<':
            self._current_x -= 1
        self.__send_location()

    def __send_location(self):
        self._path.mark_visit_to(self._current_x, self._current_y)

class Router:
    @classmethod
    def route(self, traveler, directions):
        for direction in directions:
            traveler.travel(direction)

if __name__ == "__main__":
    directions = open('day3_input.txt', 'r').read()
    traveled_path = Path()
    traveler = Traveler(traveled_path)
    Router.route(traveler, directions)
    print("Santa will visit {0} houses.".format(traveled_path.houses_visited()))
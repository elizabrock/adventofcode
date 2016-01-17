from collections import defaultdict, deque

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
    def route(self, directions, *travelers):
        travelers = deque(travelers)
        for direction in directions:
            travelers[0].travel(direction)
            travelers.rotate(1)

if __name__ == "__main__":
    directions = open('input/day3_input.txt', 'r').read()
    traveled_path = Path()
    traveler = Traveler(traveled_path)
    Router.route(directions, traveler)
    print("Santa will visit {0} houses.".format(traveled_path.houses_visited()))

    traveled_path = Path()
    traveler1 = Traveler(traveled_path)
    traveler2 = Traveler(traveled_path)
    Router.route(directions, traveler1, traveler2)
    print("Santa and Robot Santa together will visit {0} houses.".format(traveled_path.houses_visited()))
class Present:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def side_perimeters(self):
        return [
                2 * (self._length + self._width),
                2 * (self._length + self._width),
                2 * (self._width + self._height),
                2 * (self._width + self._height),
                2 * (self._height + self._length),
                2 * (self._height + self._length)
                ]

    def volume(self):
        return self._length * self._width * self._height

    def side_areas(self):
        return [
                self._length * self._width,
                self._length * self._width,
                self._width * self._height,
                self._width * self._height,
                self._height * self._length,
                self._height * self._length
                ]

    def ribbon_required(self):
        return min(self.side_perimeters()) + self.volume()

    def wrapping_paper_required(self):
        return sum(self.side_areas()) + min(self.side_areas())

class PresentCollection:
    def __init__(self, input):
        self._presents = []
        for line in input.splitlines():
            (l, w, h) = line.split('x')[0:3]
            self._presents.append(Present(int(l), int(w), int(h)))

    def wrapping_paper_required(self):
        areas = [p.wrapping_paper_required() for p in self._presents]
        return sum(areas)

    def ribbon_required(self):
        lengths = [p.ribbon_required() for p in self._presents]
        return sum(lengths)

if __name__ == "__main__":
    present_list = open('day2_input.txt', 'r').read()
    present_collection = PresentCollection(present_list)
    print("The presents will require {0} sq. ft. of wrapping paper and {1} feet of ribbon".format(present_collection.wrapping_paper_required(), present_collection.ribbon_required()))
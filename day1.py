import math

class Day1:
    @staticmethod
    def calculate(input):
        return input.count("(") - input.count(")")

advent_code = open('day1_input.txt', 'r').read()
print(Day1.calculate(advent_code))
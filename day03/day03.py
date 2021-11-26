import numpy
import string


class SantaMap:

    def __init__(self):
        self.myMap = numpy.array([0], ndmin=2)
        self.current_position = {
                          "x": 0,
                          "y": 0
        }
        self.home_position = self.current_position  # set home position

    def move(self, direction=string):
        # increase current position based on direction
        if direction == '>':
            self.current_position["x"] += 1
        elif direction == '<':
            self.current_position["x"] -= 1
        elif direction == 'v':
            self.current_position["y"] += 1
        elif direction == '^':
            self.current_position["y"] += 1

        try:
            self.myMap[self.current_position["x"], self.current_position["y"]] += 1
        except Exception as e:
            print(e)
            if direction == '>':
                self.myMap = numpy.append(self.myMap, 0, axis=1)
            elif direction == '<':
                self.myMap = numpy.insert(self.myMap, 0, 0, axis=1)
                self.home_position["x"] += 1
            elif direction == 'v':
                self.myMap = numpy.append(self.myMap, 0, axis=0)
            elif direction == '^':
                self.myMap = numpy.insert(self.myMap, 0, 0,  axis=0)
                self.home_position["y"] += 1
            self.myMap[self.current_position["x"], self.current_position["y"]] += 1
        if direction == '>':
            self.myMap[self.home_position["x"], self.home_position["y"]] += 1

    def print_result1(self):
        print("Santa has visited  " + numpy.count_nonzero(self.myMap > 0) + "houses at least once")


def read_puzzle_input(my_file=string) -> string:
    with open(my_file) as file:
        # my_boxes = file.read().splitlines()
        return file.read()


if __name__ == "__main__":
    myFile = read_puzzle_input("day03.txt")
    mySantaMap = SantaMap()
    for move in myFile:
        mySantaMap.move(move)
    pass

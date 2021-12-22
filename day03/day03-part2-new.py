import numpy
import string


class SantaMap:

    def __init__(self):
        self.myMap = numpy.array([0], dtype=int, ndmin=2)
        self.current_position = {
                          "x": 0,
                          "y": 0
        }
        self.home_position = self.current_position.copy()  # set home position
        self.santa_position = self.current_position.copy()
        self.robo_santa_position = self.current_position.copy()
        #deliver two presents to home position
        self.myMap[self.home_position["x"], self.home_position["y"]] += 2

    def move(self, direction=string, mover=string):
        if mover == "Santa":
            self.current_position = self.santa_position
        elif mover == "RoboSanta":
            self.current_position = self.robo_santa_position

        # increase current position based on direction
        if direction == '>':
            self.current_position["y"] += 1
        elif direction == '<':
            self.current_position["y"] -= 1
        elif direction == 'v':
            self.current_position["x"] += 1
        elif direction == '^':
            self.current_position["x"] -= 1

        # insert row
        if self.current_position["x"] < 0:
            self.myMap = numpy.insert(self.myMap, 0, [0], axis=0)
            self.home_position["x"] += 1
            self.current_position["x"] += 1
            if mover == "Santa":
                self.robo_santa_position["x"] += 1
            elif mover == "RoboSanta":
                self.santa_position["x"] += 1
        # insert column
        elif self.current_position["y"] < 0:
            self.myMap = numpy.insert(self.myMap, 0, 0, axis=1)
            self.home_position["y"] += 1
            self.current_position["y"] += 1
            if mover == "Santa":
                self.robo_santa_position["y"] += 1
            elif mover == "RoboSanta":
                self.santa_position["y"] += 1
        elif self.current_position["x"] == self.myMap.shape[0]:
            self.myMap = numpy.append(self.myMap, [[0 for x in range(0, self.myMap.shape[1])]], axis=0)
        elif self.current_position["y"] == self.myMap.shape[1]:
            self.myMap = numpy.append(self.myMap, [[0] for y in range(0, self.myMap.shape[0])], axis=1)

        # deliver a present to current position
        self.myMap[self.current_position["x"], self.current_position["y"]] += 1

        # deliver a present to home position
        if direction == '>':
            self.myMap[self.home_position["x"], self.home_position["y"]] += 1

    def get_num_of_houses(self):
        #print("Santa has visited  " + str(numpy.count_nonzero(self.myMap)) + " houses at least once")
         return numpy.count_nonzero(self.myMap)

def read_puzzle_input(my_file=string) -> string:
    with open(my_file) as file:
        # my_boxes = file.read().splitlines()
        return file.read()


if __name__ == "__main__":
    myFile = read_puzzle_input("day03.txt")
    #myFile = read_puzzle_input("test.txt")
    mySantaMap = SantaMap()

    #deliver present to home position:
    #mySantaMap.myMap[0, 0] += 1
    #myRoboSantaMap.myMap[0, 0] += 1
    for position, move in enumerate(myFile):
        if not position % 2:
            mySantaMap.move(move, "Santa")
        else:
            mySantaMap.move(move, "RoboSanta")
    print("Visited houses Santa and Robo-Santa: " + str(mySantaMap.get_num_of_houses()))
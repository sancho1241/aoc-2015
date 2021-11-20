import re
import string
from itertools import combinations


def read_puzzle_input (file=string) -> list:
        with open(file) as file:
            my_boxes = file.read().splitlines()
            return my_boxes


def calc_paper_for_box(my_box=string) -> int:
    '''
    example: 29 x 13 x 26
    split values with x seperator get 29 13 26 as list
    create dictionary 'l': '29', 'w': '13', 'h': '26'
    apply formular 2*lw + 2*lh + 2*wh save lowest value with first value anc comparing with others
    multiply each of them by two and add them
    calculate
    '''
    paper_for_this_box = 0
    smallest_side = 0
    my_box_sides = combinations(my_box,2) # get all possible dual combinations
    for my_box_side in my_box_sides:
        current_side = 2* int(my_box_side[0]) * int(my_box_side[1])
        if current_side/2 < smallest_side or smallest_side==0:
            smallest_side = current_side/2
        paper_for_this_box += current_side
    paper_for_this_box += smallest_side
    return paper_for_this_box
    #print("box:" + "".join(my_box))

def  calc_ribbon_for_box (my_box = string) -> int:
    ribbon_feet = 0
    my_box = sorted(my_box,reverse=True)
    ribbon_bow = 1
    for pos,side in enumerate(my_box):
        ribbon_bow *= int(side)
        if pos != 0:
            ribbon_feet += 2 * int(side)
    return ribbon_feet + ribbon_bow

if __name__ == "__main__":
    total_paper = 0
    total_ribbon = 0
    for my_box in read_puzzle_input("day02.txt"):
        print(my_box)
        my_box = re.split('x', my_box)  # split the values from the 'x'
        my_box = [int(x) for x in my_box]
        total_paper += calc_paper_for_box(my_box)
        total_ribbon += calc_ribbon_for_box(my_box)
    print ("the total amount of paper required  to wrap all boxes is " +str(total_paper) +  " square feet of paper")
    print("the total amount of ribbon required  to wrap all boxes is " + str(total_ribbon) + "  feet")
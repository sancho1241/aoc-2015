floor = 0
indexPosition = 0
with open ('input_day_01') as puzzleInput:
    for line in puzzleInput:
        print (line)
        myList = list(line)
        print (myList)
        for item in myList:
                if item == '(':
                    floor += 1
                if item == ')':
                    floor -= 1
                indexPosition+=1
                if floor == -1:
                    print ('Santa enters the basement on position:',indexPosition)
                    break
        print ('Santa needs to go to floor', floor)

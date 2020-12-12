import copy
File = open("Day11_Input.txt", "r")
Lines = File.readlines()
print(Lines)
NewLines = []
#We first add a ring of floor around the seating areas
for i in range(0,len(Lines)):
    NewLines.append(list(Lines[i].strip()))
    NewLines[i].insert(0,'.')
    NewLines[i].append('.')

NewLines.insert(0,['.']*len(NewLines[1]))
NewLines.append(['.']*len(NewLines[1]))


Lines = copy.deepcopy(NewLines)


condition = True
def checkSeats(SeatX,SeatY):
    #Direction =  N, NE, E, SE, S, SW, W,  NW
    DirectionX = [0, 1,  1,  1,  0, -1, -1, -1]
    DirectionY = [1, 1,  0, -1, -1, -1, 0,   1]

    OccupiedInView = 0
    for i in range(0,len(DirectionX)):
        # print('i',i)
        whilecounter = 1
        condition = True
        while condition == True:
            SeatXcheck = SeatX + whilecounter * DirectionX[i]
            SeatYcheck = SeatY + whilecounter * DirectionY[i]
            # print(SeatX,SeatY,SeatXcheck,SeatYcheck)
            if      SeatXcheck >= (len(Lines[0])-1) \
                    or   SeatXcheck <= 0 \
                    or   SeatYcheck <= 0 \
                    or   SeatYcheck >= (len(Lines)-1):
                # print('limit met')
                condition = False


            elif Lines[SeatYcheck][SeatXcheck] == "L":
                # print('L')
                condition = False
            elif Lines[SeatYcheck][SeatXcheck] == "#":
                OccupiedInView += 1
                # print('seat in view')
                condition = False
            # print('no cond')
            whilecounter += 1
        # print(OccupiedInView)
    return OccupiedInView





while condition == True:
    OldChanges = 0
    Changes = 0
    print("While loop")
    NewLines = copy.deepcopy(Lines)

    for i in range(1,len(Lines)-1):
        print(Lines[i])
        for j in range(1,len(Lines[i])-1):
            # print(j)
            if Lines[i][j] == "L":
                # print(checkSeats(i,j))
                if checkSeats(j,i) == 0:
                    NewLines[i][j] = "#"
                    Changes += 1

            if Lines[i][j] == "#":
                if checkSeats(j, i) >= 5:
                    NewLines[i][j] = "L"
                    Changes += 1


    print(OldChanges,Changes)
    if OldChanges == Changes:
        condition = False
    Lines = copy.deepcopy(NewLines)
    OldChanges = Changes

Seats = 0
for Line in Lines:
    Seats += Line.count("#")
print(Seats)




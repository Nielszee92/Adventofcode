import copy
import math
File = open("Day12_Input.txt", "r")
Lines = File.readlines()

Heading = 0
PositionX = 0
PositionY = 0

Instruction = ["N","E","S","W"]
DirectionX =  [0, 1,  0,  -1]
DirectionY =  [1, 0,  -1,  0]
#Only L and R change the heading
for Line in Lines:
    Step = int(Line[1:])
    print(Step)
    if Line[0] == "L":
        Heading += Step*(math.pi/180)
    elif Line[0] == "R":
        Heading -= Step*(math.pi/180)
    elif Line[0] == "F":
        PositionX += int(math.cos(Heading)) * Step
        PositionY += int(math.sin(Heading)) * Step
    else:
        Index = Instruction.index(Line[0])
        PositionX += DirectionX[Index]*Step
        PositionY += DirectionY[Index]*Step
    print(PositionX,PositionY)






import copy
import math
File = open("Day12_Input.txt", "r")
Lines = File.readlines()

PositionX = 0
PositionY = 0
WayPointX = 10
WayPointY = 1

Instruction = ["N","E","S","W"]
DirectionX =  [0, 1,  0,  -1]
DirectionY =  [1, 0,  -1,  0]
#Only L and R change the heading
for Line in Lines:
    Step = int(Line[1:])
    print(Line)
    print(Step)
    if Line[0] == "L":
        Angle = int(Line[1:])*math.pi/180
        print(Angle, math.cos(Angle), math.sin(Angle))
        NewWayPointX = (WayPointX) * (math.cos(Angle)) - (WayPointY) * math.sin(Angle)
        NewWayPointY = (WayPointX) * (math.sin(Angle)) + (WayPointY) * math.cos(Angle)
        WayPointX = round(NewWayPointX)
        WayPointY = round(NewWayPointY)
    elif Line[0] == "R":
        Angle = -int(Line[1:]) * math.pi / 180
        NewWayPointX = ( WayPointX) * (math.cos(Angle)) - ( WayPointY) * math.sin(Angle)
        NewWayPointY = ( WayPointX) * (math.sin(Angle)) + ( WayPointY) * math.cos(Angle)
        WayPointX = round(NewWayPointX)
        WayPointY = round(NewWayPointY)
    elif Line[0] == "F":
        PositionX += WayPointX * Step
        PositionY += WayPointY * Step
    else:
        Index = Instruction.index(Line[0])
        WayPointX += DirectionX[Index]*Step
        WayPointY += DirectionY[Index]*Step
    print("pos",PositionX,PositionY)
    print("way",WayPointX,WayPointY)
print(abs(PositionX)+abs(PositionY))





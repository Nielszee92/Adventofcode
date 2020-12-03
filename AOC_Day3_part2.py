import re
File = open("Day3_Input.txt", "r")
Lines = File.readlines()
Trees = 0
PosX = -3

def checkTrees(StepX,StepY,Lines):
    PosX = -StepX
    StartY = 0
    Trees = 0
    for i in range(0,int((len(Lines))/StepY)):
        PosY = StartY + i*StepY
        PosX += StepX
        if PosX > 30:
            print('corr')
            PosX -= 31
        List = list(Lines[PosY].strip())
        print(List)
        print(PosX,PosY)
        if List[PosX] == "#":
            Trees += 1
    return Trees

Trees1 = checkTrees(1,1,Lines)
Trees2 = checkTrees(3,1,Lines)
Trees3 = checkTrees(5,1,Lines)
Trees4 = checkTrees(7,1,Lines)
Trees5 = checkTrees(1,2,Lines)
print(Trees1,Trees2,Trees3,Trees4,Trees5)
print(Trees1*Trees2*Trees3*Trees4*Trees5)
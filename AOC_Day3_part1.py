import re
File = open("Day3_Input.txt", "r")
Lines = File.readlines()
Trees = 0
PosX = -3
for i in range(0,len(Lines)):
    List = Lines[i].strip()
    PosX += 3
    if PosX > 30:
        PosX -= 31
    List = list(Lines[i].strip())


    if List[PosX] == "#":
        Trees += 1
        List[PosX] = "T"
    else:
        List[PosX] = "O"
    print(List)
print(Trees)

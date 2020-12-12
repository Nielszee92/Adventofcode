import copy
File = open("Day11_Input.txt", "r")
Lines = File.readlines()
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

while condition == True:
    OldChanges = 0
    Changes = 0
    print("While loop")

    for i in range(1,len(Lines)-1):
        for j in range(1,len(Lines[i])-1):
            if Lines[i][j] == "L":
                Counter = 0
                #Check if adjacent seats are empty
                for k in [i-1,i,i+1]:
                    for l in [j-1,j,j+1]:
                        if k== i and l == j:
                            pass
                        else:
                            if Lines[k][l] == "#":
                                Counter += 1
                if Counter == 0:
                    NewLines[i][j] = "#"
                    Changes += 1
            if Lines[i][j] == "#":
                Counter = 0
                # Check if 4 or more adjacent seats are occupied
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        if k== i and l == j:
                            pass
                        else:
                            if Lines[int(k)][int(l)] == "#":
                                Counter += 1
                if Counter >= 4:
                    NewLines[i][j] = "L"
                    Changes += 1
        print('after  :',NewLines[i])
    print(OldChanges,Changes)
    if OldChanges == Changes:
        condition = False
    Lines = copy.deepcopy(NewLines)
    OldChanges = Changes

Seats = 0
for Line in Lines:
    Seats += Line.count("#")
print(Seats)




import numpy as np

File = open("Day10_Input.txt", "r")
Lines = File.readlines()

Array = [0]
for Line in Lines:
    Array.append(float(Line.strip()))
print(Array)
Array.append(max(Array)+3)
print(Array)

NPArray = np.array(Array)
SortedNParray = np.sort(NPArray)
print(SortedNParray)
JoltJumps = []
Ones = 0
Threes = 0
Correction = 0
for i in range(0,len(SortedNParray)-1):
    JoltJumps.append(SortedNParray[i+1]-SortedNParray[i])
    if SortedNParray[i+1]-SortedNParray[i] == 1:
        Ones += 1
    if SortedNParray[i+1]-SortedNParray[i] == 3:
        Threes += 1
Whilecounter1 = 0

List = []
while Whilecounter1 < len(JoltJumps):
    print(Whilecounter1)
    print(JoltJumps[Whilecounter1])
    if JoltJumps[Whilecounter1] == 1:
        Whilecounter2 = 0
        while JoltJumps[Whilecounter1+Whilecounter2] != 3:
            print(Whilecounter1+Whilecounter2)
            print(JoltJumps[Whilecounter1+Whilecounter2])
            Whilecounter2 += 1
        List.append(Whilecounter2-1)
        Whilecounter1 += Whilecounter2
    Whilecounter1 += 1
print(JoltJumps)
print(List)

Count = 1
for ele in List:
    MinSteps = int(ele/3)
    print(ele,MinSteps)
    print(2**(ele)-(MinSteps))
    Count = Count * (2**(ele)-(MinSteps))
print(Count)


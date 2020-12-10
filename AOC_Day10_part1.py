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
for i in range(0,len(SortedNParray)-1):
    JoltJumps.append(SortedNParray[i+1]-SortedNParray[i])
    if SortedNParray[i+1]-SortedNParray[i] == 1:
        Ones += 1
    if SortedNParray[i+1]-SortedNParray[i] == 3:
        Threes += 1
print(JoltJumps)
print(Ones*Threes)





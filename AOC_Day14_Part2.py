import copy
import math
import numpy as np
from itertools import product

File = open("Day14_Input.txt", "r")
Lines = File.readlines()

List = []
for i in range(0,36):
    List.append(2**(35-i))

def getValue(Number):
    value = ""
    Delta = Number
    for i in range(0,36):
        if List[i] <= Delta:
            Delta = Delta - List[i]
            value += "1"
        else:
            value += "0"
    return value

def CalculateNumber(IndexStr, Mask,memory,Number):
    CountX = Mask.count("X")
    print("Count X:",CountX)
    Combinations= list(product([0, 1], repeat=CountX))
    print(Combinations[0][0])

    Numbers = []
    NewMask = ""
    #First calucate the mask:
    for i in range(0, len(IndexStr)):
        if Mask[i] == "1":
            NewMask += '1'
        elif Mask[i] == "0":
            NewMask += IndexStr[i]
        else:
            NewMask += 'X'

    # Create mask for each combination
    for j in range(0,2**CountX):
        print('j',j)
        counter = 0
        CombinationMask = ""
        for ele in NewMask:
            if ele == "X":
                CombinationMask += str(Combinations[j][counter])
                counter += 1
            else:
                CombinationMask += ele
        print('NewMas   ',CombinationMask)
        print('IndexStr ',IndexStr)
        NewIndex = 0
        for i in range(0, len(IndexStr)):
            if CombinationMask[i] == "1":
                NewIndex += List[i]
            else:
                pass

        print(NewIndex)
        memory[NewIndex] = Number

    return  memory


memory = {}
for Line in Lines:
    if "mask = " in Line:
        Mask = Line.strip().split(" ")[2]
        print(Mask)
    if "mem" in Line:
        Index = Line.strip().split(" ")[0].replace("mem[","").replace("]","")
        Number = Line.strip().split(" ")[2]
        print(Index,Number)
        IndexStr = getValue(float(Index))
        print(IndexStr)
        memory = CalculateNumber(IndexStr, Mask,memory,Number)
print(memory)

Sum = 0
for ele in memory:
    Sum += float(memory[ele])

print(Sum)





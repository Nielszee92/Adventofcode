import copy
import math
import numpy as np
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

def CalculateNumber(Value,Mask):
    NewValue = ""
    NewNumber = 0
    for i in range(0,len(Value)):
        if Value[i] == "1" and Mask[i] == "X":
            NewValue += "1"
            NewNumber += List[i]
        elif Value[i] == "1" and Mask[i] == "1":
            NewValue += "1"
            NewNumber += List[i]
        elif Value[i] == "1" and Mask[i] == "1":
            NewValue += "1"
            NewNumber += List[i]
        elif Value[i] == "0" and Mask[i] == "1":
            NewValue += "1"
            NewNumber += List[i]
        else:
            NewValue += "0"
    print(Value)
    print(Mask)
    print(NewValue)
    print(NewNumber)

    return NewValue, NewNumber


memory = {}
for Line in Lines:
    if "mask = " in Line:
        Mask = Line.strip().split(" ")[2]
        print(Mask)
    if "mem" in Line:
        Index = Line.strip().split(" ")[0].replace("mem[","").replace("]","")
        Number = Line.strip().split(" ")[2]
        print(Index,Number)
        Value = getValue(float(Number))
        NewValue, NewNumber = CalculateNumber(Value, Mask)
        memory[Index] = NewNumber
print(memory)

Sum = 0
for ele in memory:
    Sum += float(memory[ele])

print(Sum)





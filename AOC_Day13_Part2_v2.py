import copy
import math
File = open("Day13_Input.txt", "r")
Lines = File.readlines()


BusTimes = Lines[1].strip().split(',')

Busses = []
Indices = []

for i in range(0,len(BusTimes)):
    if BusTimes[i] != "x":
        Busses.append(float(BusTimes[i]))
        Indices.append(i)

MaxStep = max(Busses)
MaxIndex = Indices[Busses.index(MaxStep)]
print(Indices)

TimeCorrection= [x - MaxIndex for x in Indices]
print(Busses)
print(TimeCorrection)
print(MaxStep,MaxIndex)


condition1 = False
StartTime = 0
T0 = 0
TimeStampDelta = MaxStep
Timestamp = T0

time = 0
stepsize = 1
print('starting loop')
for i in range(0,len(Busses)-1):
    print(Busses[i])
    condition = False
    stepsize *= Busses[i]
    print(stepsize)

    while condition == False:
        print(time)
        nextdeparture = time + Indices[i+1]
        if nextdeparture % Busses[i+1] == 0:
            condition = True
        else:
            time += stepsize






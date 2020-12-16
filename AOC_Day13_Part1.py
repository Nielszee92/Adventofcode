import copy
import math
File = open("Day13_Input.txt", "r")
Lines = File.readlines()

ArrivalTime = float(Lines[0])

BusTimes = Lines[1].strip().split(',')

BusID = 0
WaitingTime = 9999999.0
for bus in BusTimes:
    if bus == "x":
        pass
    else:
        Delta = math.floor(ArrivalTime/float(bus))+1
        WaitingTimeX = Delta*float(bus)-ArrivalTime
        if WaitingTimeX < WaitingTime:
            BusID = bus
            WaitingTime = WaitingTimeX
            print('result',BusID,WaitingTime)
print(WaitingTime,BusID)
print(int(WaitingTime)*int(BusID))





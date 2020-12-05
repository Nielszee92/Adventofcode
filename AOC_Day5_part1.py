import re
import pandas as pd
import openpyxl
import numpy as np
File = open("Day5_Input.txt", "r")
Lines = File.readlines()

List = np.linspace(0, 127, 128)


def getMinMax(List,Letter):
    if Letter == "F" or Letter == "L":
         NewList = List[0:int(len(List)/2)]
    else:
         NewList = List[int(len(List)/2):int(len(List))]

    return NewList
MaxRow = 0
TakenSeats = []
Data = [[],[]]
for Line in Lines:
     List = np.linspace(0, 127, 128)
     print(Line[0:7])
     print(Line[8:10])
     for ele in Line[0:6]:
         List = getMinMax(List,ele)
     if Line[6] == "F":
          Row = List[0]
     else:
          Row = List[1]
     List = np.linspace(0, 7, 8)
     for ele in [Line[7],Line[8],Line[9]]:
          List= getMinMax(List, ele)
     Col = List[0]
     if float(Row) > MaxRow:
          MaxRow = Row
          ColMax = Col
     elif Row == MaxRow:
          if float(Col) > ColMax:
               ColMax = Col
     print('Row = {0} and Col = {1}'.format(Row,Col))
     if float(Row) > 1 and float(Row) < 126:
          SeatID = float(Row)*8+float(Col)
          TakenSeats.append(SeatID)
          Data[0].append(Row)
          Data[1].append(Col)



Array = np.array(TakenSeats)
print(len(Array))
Array.sort()
print(Array)
print(len(Array))
for i in range(1,len(Array)-1):
     if Array[i+1]-Array[i] == 2:
          MySeatID = Array[i]+1
          print(MySeatID)


import copy
import math
import numpy as np
from itertools import product

StartingNumbers = [6,13,1,15,2,0]

Turn = 0
SpokenNumbers = {}
for i in range(0,30000000):
    # print(SpokenNumbers)
    Turn += 1

    if i < len(StartingNumbers):
        NewNumber = StartingNumbers[i]
        if NewNumber in SpokenNumbers.keys():
            SpokenNumbers[NewNumber].append(Turn)
        else:
            SpokenNumbers[NewNumber] = [Turn]

    else:
        if len(SpokenNumbers[OldNumber]) == 1:
            NewNumber = 0
            if NewNumber in SpokenNumbers.keys():
                SpokenNumbers[NewNumber].append(Turn)
            else:
                SpokenNumbers[NewNumber] = [Turn]
        else:
            # print(SpokenNumbers[OldNumber][-1],SpokenNumbers[OldNumber][-2])
            NewNumber = SpokenNumbers[OldNumber][-1]-SpokenNumbers[OldNumber][-2]
            if NewNumber in SpokenNumbers.keys():
                SpokenNumbers[NewNumber].append(Turn)
            else:
                SpokenNumbers[NewNumber] = [Turn]
    OldNumber = NewNumber
print("Turn = ",Turn," number = ",NewNumber)
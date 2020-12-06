import re
import pandas as pd
import openpyxl
import numpy as np
File = open("Day6_Input.txt", "r")
Lines = File.readlines()

Points = 0
condition = False
Group = []
LineCounter = 0
for Line in Lines:
    LineCounter += 1
    if condition == False:
        for ele in Line.strip():
            Group.append(ele)
    if Line.strip() == "" or LineCounter == len(Lines):
        LettersArray = np.array(Group)
        Letters = np.unique(Group)
        print(Letters)
        Points += len(Letters)
        Group = []
print(LineCounter,len(Lines))
print(Points)

import re
import pandas as pd
import openpyxl
import numpy as np
File = open("Day6_Input.txt", "r")
Lines = File.readlines()

Points = 0
condition = False
Group = []
GroupLines = []
LineCounter = 0
for Line in Lines:
    # print(Line)
    if condition == False:
        for ele in Line.strip():
            Group.append(ele)
            GroupLines.append(LineCounter)
    LineCounter += 1
    if Line.strip() == "" or LineCounter == len(Lines):
        LettersArray = np.array(Group)
        Letters = np.unique(Group)
        # print(Letters)
        # print(GroupLines)
        for Letter in Letters:
            AllTrue = True
            for LetterLine in GroupLines:
                if Letter not in Lines[LetterLine]:
                    AllTrue = False
            if AllTrue == True:
                # print(Letter,'points')
                Points += 1

        Group = []
        GroupLines = []
print(Points)

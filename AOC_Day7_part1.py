File = open("Day7_Input.txt", "r")
Lines = File.readlines()
ContainsShinyGold = 0
BagColors = []
BagContainsColors = []
CheckColors = []
NewCheckColors = []

for Line in Lines:
    BagColor = Line.split("contain")[0][:-5]
    BagColors.append(BagColor)
    InBag = Line.strip().split("contain")[1]
    BagsInBag = InBag.split(",")

    Colors = []
    for ele in BagsInBag:
        if "shiny gold" in ele:
            ContainsShinyGold += 1
            CheckColors.append(BagColor)
            NewCheckColors.append(BagColor)
        if "no other bags" not in ele:
            Colors.append(ele.split(" ")[2] + " " + ele.split(" ")[3])
        else:
            Colors.append("")


    BagContainsColors.append(Colors)


condition = True
NewColors = []
while condition == True:
    print('While Loop')
    Before = len(CheckColors)
    print('Before:',Before)
    print(CheckColors)
    for Color in CheckColors:
        print(Color)
        for i in range(0,len(BagColors)):
            if str(Color.strip()) in list(BagContainsColors[i]):
                if BagColors[i] not in CheckColors:
                    ContainsShinyGold += 1
                    NewCheckColors.append(BagColors[i])

    CheckColors = NewCheckColors

    After = len(CheckColors)
    print('After:',After)
    print(CheckColors)
    if Before == After:
        condition = False


print(ContainsShinyGold)
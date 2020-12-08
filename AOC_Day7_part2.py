#My code didnt work; all credits to https://www.youtube.com/watch?v=4Fr1zSzaUyY

rules = dict()

with open("Day7_Input.txt") as file:
    data = file.read()
    data = data.replace(".","")
    data = data.replace(" no other bags","")
    data = data.replace(" bags","")
    data = data.replace(" bag","")
    data = data.split("\n")
    for line in data:
        line = line.split(" contain ")
        left = line[0]
        right = []
        if len(line) > 1:
            line = line[1].split(", ")
            for element in line:
                value = element.split(" ", 1)[0]
                if value != "no":
                    value = int(value)
                    name = element.split(" ",1)[1]
                    right.append([value,name])
        rules[left] = right
#
# File = open("Day7_Input.txt", "r")
# Lines = File.readlines()
# rules = dict()
# BagColors = []
# BagContainsColors = []
# CheckColors = []
# NewCheckColors = []
#
# for Line in Lines:
#     BagColor = Line.split("contain")[0][:-5]
#     BagColors.append(BagColor)
#     InBag = Line.strip().split("contain")[1]
#     BagsInBag = InBag.split(",")
#
#     Colors = []
#     for ele in BagsInBag:
#         if "no other bags" not in ele:
#             Colors.append([int(ele.split(" ")[1]),ele.split(" ")[2] + " " + ele.split(" ")[3]])
#         else:
#             Colors.append("")
#     if "clear violet" in BagColor:
#     if len(Colors)== 1:
#         pass
#     else:
#         rules[BagColor.strip()] = Colors
#     BagContainsColors.append(Colors)



total = -1

bags = { 'shiny gold' : 1 }
while len(bags) > 0:
    key = list(bags.keys())[0]
    print(key)
    total += bags[key]
    if key in rules:
        for newbag in rules[key]:
            if newbag[1] not in bags:
                bags[newbag[1]] = 0
            bags[newbag[1]] += (list(bags.values())[0]*newbag[0])
    del bags[key]


print(total)
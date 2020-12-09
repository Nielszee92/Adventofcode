File = open("Day9_Input.txt", "r")
Lines = File.readlines()

preamble = 25

for i in range(preamble,len(Lines)):
    print(i)
    Number = float(Lines[i].strip())
    #Check if previous numbers can sum up to this Number:
    condition = False
    for j in range(i-25,i-1):
        for k in range(j+1,i):
            print(float(Lines[j].strip()),float(Lines[k].strip()),float(Lines[j].strip()) + float(Lines[k].strip()),Number)
            if (float(Lines[j].strip()) + float(Lines[k].strip())) == Number:
                condition = True
    if condition == False:
        print(Number)
        break

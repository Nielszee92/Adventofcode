File = open("Day1_Input.txt", "r")
Lines = File.readlines()
condition = False

for i in range(0,len(Lines)):
    for j in range(i,len(Lines)):
        #print(Lines[i],Lines[j])
        for k in range(j,len(Lines)):
            if float(Lines[i])+float(Lines[j])+float(Lines[k]) == 2020:
                condition = True
                print(i,j)
                print(Lines[i],Lines[j],Lines[k])
                print(float(Lines[i])*float(Lines[j])*float(Lines[k]))


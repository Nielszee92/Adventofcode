File = open("Day8_Input.txt", "r")
Lines = File.readlines()


def CheckBoot(BootLines):
    ExecutedLines = [0]
    Accumulator = 0
    condition = True
    ExecuteLine = 0
    while condition == True:
        print(ExecuteLine)

        Line = BootLines[ExecuteLine]
        Commands = Line.split(" ")
        Command = Commands[0].strip()
        Step = int(Commands[1].strip())
        if Command == "nop":
            NewExecuteline = ExecuteLine + 1
        if Command == "acc":
            Accumulator += Step
            NewExecuteline = ExecuteLine + 1
        if Command == "jmp":
            NewExecuteline = ExecuteLine + Step

        if NewExecuteline in ExecutedLines:
            condition = False
        if ExecuteLine == len(BootLines)-1:
            break
        print("Executeline =", BootLines[ExecuteLine])
        print("Accumulator = ", Accumulator)
        ExecutedLines.append(NewExecuteline)
        ExecuteLine = NewExecuteline
    return condition,Accumulator

for i in range(0,len(Lines)):
    NewLines = Lines.copy()

    if "nop" in Lines[i]:
        ChangedLine = Lines[i]
        ChangedLine = ChangedLine.strip().replace("nop", "jmp")
        NewLines[i] = ChangedLine
        condition, Accumulator = CheckBoot(NewLines)
        # print(condition,Accumulator)
        if condition == True:
            print(Accumulator)
            break
        print(i, condition, Accumulator)
    if "jmp" in Lines[i]:
        ChangedLine = Lines[i]
        ChangedLine = ChangedLine.strip().replace("jmp", "nop")
        NewLines[i] = ChangedLine
        condition, Accumulator = CheckBoot(NewLines)
        # print(condition,Accumulator)
        if condition == True:
            print(Accumulator)
            break
        print(i,condition,Accumulator)



File = open("Day9_Input.txt", "r")
Lines = File.readlines()

preamble = 25

KeyNumber = 25918798
for i in range(0,len(Lines)):
    print(i)
    Sum = 0
    List = []
    whilecounter = 0
    while Sum < KeyNumber:
        Sum += float(Lines[i+whilecounter].strip())
        List.append(float(Lines[i+whilecounter].strip()))
        whilecounter += 1

    if Sum == KeyNumber:
        print('found solution:')
        print(min(List))
        print(max(List))
        print(min(List)+max(List))




import re
File = open("Day2_Input.txt", "r")
Lines = File.readlines()
Valid = 0
for i in range(0,len(Lines)):
    S = re.split(r'[-:,\s]\s*', Lines[i])

    Amount = 0
    print(S)
    for letter in S[3]:
        #print(letter)
        if letter == S[2]:
            Amount += 1
            #print(Amount)
    #print(S[0], "<=", Amount, ">=", S[1])
    if Amount >= int(S[0]) and Amount <= int(S[1]):
        print('valid',Valid)
        #print(S[0], "<=",Amount, ">=", S[1])
        Valid += 1

print(Valid)
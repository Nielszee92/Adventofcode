import re
File = open("Day2_Input.txt", "r")
Lines = File.readlines()
Valid = 0
for i in range(0,len(Lines)):
    S = re.split(r'[-:,\s]\s*', Lines[i])

    Amount = 0
    print(S)
    print(S[2], S[3][int(S[0])-1], S[3][int(S[1])-1])

    if S[2] == S[3][int(S[0])-1] and S[2] != S[3][int(S[1])-1] or S[2] != S[3][int(S[0])-1] and S[2] == S[3][int(S[1])-1]:

        print('valid',Valid+1)
        #print(S[0], "<=",Amount, ">=", S[1])
        Valid += 1

print(Valid)
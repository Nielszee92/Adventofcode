import re
import pandas as pd
import openpyxl

File = open("Day4_Input.txt", "r")
Lines = File.readlines()
List = []
EmptyLine = False
RequiredFields = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]
ValidPassports = 0
ValidatedPassports = 0

global byrList,iyrList,eyrList,hgtList,hclList,eclList,eclList,pidList

byrList = []
iyrList = []
eyrList = []
hgtList = []
hclList = []
eclList = []
pidList = []



def ValidateFields(Passport):
    Valid = True
    byr = Passport[Passport.index('byr') + 1]
    byrList.append(byr)
    if float(byr) < 1920 or float(byr) > 2002:
        print('wrong birth year')
        Valid = False
    iyr = Passport[Passport.index('iyr') + 1]
    iyrList.append(iyr)
    if float(iyr) < 2010 or float(iyr) > 2020:
        print('wrong issue year')
        Valid = False
    eyr = Passport[Passport.index('eyr')+1]
    eyrList.append(eyr)
    if float(eyr) < 2020 or float(eyr) > 2030:
        print('wrong expire year')
        Valid = False
    hgt = Passport[Passport.index('hgt') + 1]
    hgtList.append(hgt)
    if "cm" not in hgt and "in" not in hgt:
        Valid = False
    if "cm" in hgt:
        if float(hgt[:-2]) < 150 or float(hgt[:-2]) > 193:
            print('wrong hgt')
            Valid = False
    if "in" in hgt:
        if float(hgt[:-2]) < 59 or float(hgt[:-2]) > 76:
            print('wrong hgt')
            Valid = False

    hcl = Passport[Passport.index('hcl') + 1]
    hclList.append(hcl)
    if hcl[0] != "#":
        Valid = False
        print('wrong hcl')
    else:
        if len(hcl) == 7:
            for j in range(1,6):
                Check = ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
                if hcl[j] not in Check:
                    Valid = False
                    print('wrong hcl',hcl[j])
    ecl = Passport[Passport.index('ecl') + 1]
    eclList.append(ecl)
    if ecl not in ["amb","blu","brn","gry","grn","hzl","oth"]:
        Valid = False
        print('Wrong ecl')
    pid = Passport[Passport.index('pid') + 1]
    pidList.append(pid)
    print(len(pid))
    if len(pid) == 9:
        for number in pid:
            try:
                int(number)
            except:
                print('error converting int')
                Valid = False
    else:
        Valid = False
    print(Valid)

    return Valid



for i in range(0,len(Lines)):
    #print(i,"/",len(Lines)-1)
    if Lines[i].strip() == "":
        EmptyLine = True
        #Do Check
        Passport = []
        for line in List:
            items = re.split(r'[\s:]', line)
            for ele in items:
                Passport.append(ele)
        print(Passport)
        PassportValid = True
        for field in RequiredFields:
            if field not in Passport:
                PassportValid = False
        if PassportValid == True:
            print("Passport is valid")
            if ValidateFields(Passport) == True:
                ValidatedPassports += 1
                print("Passport is validated")
            ValidPassports += 1
        List = []
        EmptyLine = False
    if EmptyLine == False:
        List.append(Lines[i].strip())
    if i == len(Lines)-1:
        Passport = []
        for line in List:
            items = re.split(r'[\s:]', line)
            for ele in items:
                Passport.append(ele)
        print(Passport)
        PassportValid = True
        for field in RequiredFields:
            if field not in Passport:
                PassportValid = False
        if PassportValid == True:
            print("Passport is valid")
            if ValidateFields(Passport) == True:
                print("Passport is validated")
                ValidatedPassports += 1
            ValidPassports += 1

        List = []
        EmptyLine = False

Data = pd.DataFrame()

Data['byr'] = byrList
Data['iyr'] = iyrList
Data['eyr'] = eyrList
Data['hgt'] = hgtList
Data['hcl'] = hclList
Data['ecl'] = eclList
Data['pid'] = pidList

writer = pd.ExcelWriter("Test.xlsx", engine='openpyxl')
workbook = writer.book
Data.to_excel(writer, sheet_name="test", startrow=0, startcol=0)
writer.save()
print("Number of valid passports:", ValidPassports)

print("Number of validated passports:", ValidatedPassports)

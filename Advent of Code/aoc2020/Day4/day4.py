def partOne(arr:list):
    dicPass = {'byr':1, 'iyr':2, 'eyr':3, 'hgt':4, 'hcl':5, 'ecl':6, 'pid':7, 'cid':8}
    passportValidOne = {1,2,3,4,5,6,7,8}
    passportValidTwo = {1,2,3,4,5,6,7}
    cont = 0   
    aux = set()

    newArr = []
    for i in arr:
        partArr = i.split(" ")
        for k in partArr:
            newArr.append(k)

    for mypass in newArr:
        if mypass == '':
            aux.clear()
            continue
        

        if "byr:" in mypass:
            #4 digits
            if len(mypass.split(":")[1]) != 4:
                aux.clear()
                continue
            #1920-2002
            if int(mypass.split(":")[1]) < 1920 or int(mypass.split(":")[1]) > 2002:
                aux.clear()
                continue
            aux.add(dicPass['byr'])
          
        if "iyr:" in mypass:
            #4 digits
            if len(mypass.split(":")[1]) != 4:
                aux.clear()
                continue
            #2010-2020
            if int(mypass.split(":")[1]) < 2010 or int(mypass.split(":")[1]) > 2020:
                aux.clear()
                continue
            aux.add(dicPass['iyr'])

        if "eyr:" in mypass:
            #4 digits
            if len(mypass.split(":")[1]) != 4:
                aux.clear()
                continue
            #2020-2030
            if int(mypass.split(":")[1]) < 2020 or int(mypass.split(":")[1]) > 2030:
                aux.clear()
                continue
            aux.add(dicPass['eyr'])

        if "hgt:" in mypass:
            if "cm" in mypass:
                #150-193
                if int(mypass.split(":")[1].replace("cm", "")) < 150 or int(mypass.split(":")[1].replace("cm", "")) > 193:
                    aux.clear()
                    continue
                aux.add(dicPass['hgt'])
            if "in" in mypass:
                #59-76
                if int(mypass.split(":")[1].replace("in", "")) < 59 or int(mypass.split(":")[1].replace("in", "")) > 76:
                    aux.clear()
                    continue
                aux.add(dicPass['hgt'])
            

        if "hcl:" in mypass:
            #start with #
            if mypass.split(":")[1][0] != "#":
                aux.clear()
                continue
            #6 digits
            if len(mypass.split(":#")[1]) != 6:
                aux.clear()
                continue
            #color valid
            for bucle in mypass.split(":#")[1]:
                if bucle not in "0123456789abcdef":
                    aux.clear()
                    continue
    
            aux.add(dicPass['hcl'])

        if "ecl:" in mypass:
            #color valid
            if mypass.split(":")[1] not in "amb blu brn gry grn hzl oth":
                aux.clear()
                continue
            aux.add(dicPass['ecl'])
        if "pid:" in mypass:
            #9 digits
            if len(mypass.split(":")[1]) != 9:
                aux.clear()
                continue
            
            aux.add(dicPass['pid'])
        if "cid:" in mypass:
            aux.add(dicPass['cid'])

        if passportValidOne == aux or passportValidTwo == aux:
            cont += 1
            aux.clear()

    print(cont)
        




def getList():
    with open("Advent of Code\\aoc2020\Day4\day4info.txt") as f:
        return [str(line.strip()) for line in f]

partOne(getList())
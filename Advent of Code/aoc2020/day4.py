def partOne(arr:list):
    dicPass = {'byr':1, 'iyr':2, 'eyr':3, 'hgt':4, 'hcl':5, 'ecl':6, 'pid':7, 'cid':8}
    passportValidOne = {1,2,3,4,5,6,7,8}
    passportValidTwo = {1,2,3,4,5,6,7}
    cont = 0
    
    aux = set()
    for mypass in arr:
        if mypass == '':
            aux.clear()
            continue

        if "byr:" in mypass:
            
            aux.add(dicPass['byr'])
        if "iyr:" in mypass:
            aux.add(dicPass['iyr'])
        if "eyr:" in mypass:
            aux.add(dicPass['eyr'])
        if "hgt:" in mypass:
            aux.add(dicPass['hgt'])
        if "hcl:" in mypass:
            aux.add(dicPass['hcl'])
        if "ecl:" in mypass:
            aux.add(dicPass['ecl'])
        if "pid:" in mypass:
            aux.add(dicPass['pid'])
        if "cid:" in mypass:
            aux.add(dicPass['cid'])

        if passportValidOne == aux or passportValidTwo == aux:
            cont += 1
            aux.clear()
    print(cont)
        




def getList():
    with open("Advent of Code\\aoc2020\\day4info.txt") as f:
        return [str(line.strip()) for line in f]

partOne(getList())
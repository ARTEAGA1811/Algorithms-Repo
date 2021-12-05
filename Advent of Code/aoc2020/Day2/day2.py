def part1(arr: list):
    myCount = 0
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
        aux = arr[i].split(" ")
        listRange = aux[0].split("-")
        letter = aux[1][0]
        password = aux[2]
        if (int(listRange[0]) <= password.count(letter) <= int(listRange[1])):
            myCount += 1
    
    return myCount


def partTwo(arr:list):
    myCount = 0
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
        aux = arr[i].split(" ")
        listRange = aux[0].split("-")
        letter = aux[1][0]
        password = aux[2]
        if ((password[int(listRange[0])-1] == letter and password[int(listRange[1])-1] != letter)
            or (password[int(listRange[0])-1] != letter and password[int(listRange[1])-1] == letter)):
            myCount += 1
    return myCount


def getList():
    with open("Advent of Code\\aoc2020\day2info.txt") as f:
        return [str(line.strip()) for line in f]

print(partTwo(getList()))
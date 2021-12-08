def day6puzzle2(answers:list):
    sumTotal = 0
    wordsUsed = {}
    numPersons  = 0
    for an in answers:
        if an == "":
            for key, value in wordsUsed.items():
                if value == numPersons:
                    sumTotal += 1     
            wordsUsed = {}
            numPersons = 0
        else:
            for i in an:
                if i not in wordsUsed:
                    wordsUsed[i] = 1
                else:
                    wordsUsed[i] += 1
            numPersons += 1

    for key, value in wordsUsed.items():
        if value == numPersons:
            sumTotal += 1 
    return sumTotal


def getList():
    with open("Advent of Code\\aoc2020\Day6\day6info.txt") as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day6puzzle2(getList()))
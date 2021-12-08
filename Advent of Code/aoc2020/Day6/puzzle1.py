def day6puzzle1(answers:list):
    sumTotal = 0
    wordsUsed = set()
    for an in answers:
        if an == "":
            sumTotal+=len(wordsUsed)
            wordsUsed = set()
        else:
            for i in an:
                wordsUsed.add(i)
 
    sumTotal+=len(wordsUsed)
    return sumTotal


def getList():
    with open("Advent of Code\\aoc2020\Day6\day6info.txt") as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day6puzzle1(getList()))
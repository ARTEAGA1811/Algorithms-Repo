def getRow(rows:str):
    left = 0
    right = 127
    for i in rows:
        if i == "F":
            right = (left+right)//2
        elif i == "B":
            left = ((left+right)//2)+1
    return left

def getColumn(columns:str):
    left = 0
    right = 7
    for i in columns:
        if i == "L":
            right = (left+right)//2
        elif i == "R":
            left = ((left+right)//2)+1
    return left

def day5puzzle1(binSpaceList:list):
    maxId = 0
    for i in range(len(binSpaceList)):
        rows = binSpaceList[i][:7]
        cols = binSpaceList[i][7:]
        maxId = max(maxId, getRow(rows)*8+getColumn(cols))
    return maxId



def getList():
    with open("Advent of Code\\aoc2020\Day5\day5info.txt") as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day5puzzle1(getList()))
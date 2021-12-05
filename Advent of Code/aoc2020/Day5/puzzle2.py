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

def getAllPossibleIds():
    allIds = set()
    for i in range(128):
        for j in range(8):
            allIds.add(i*8+j)
    return allIds
 
def day5puzzle1(binSpaceList:list):
    allIds = getAllPossibleIds()
    myIds = set()
    for i in range(len(binSpaceList)):
        rows = binSpaceList[i][:7]
        cols = binSpaceList[i][7:]
        myIds.add(getRow(rows)*8+getColumn(cols))
    
    rest = allIds - myIds
    for i in rest:
        if i+1 in myIds and i-1 in myIds:
            return i



def getList():
    with open("Advent of Code\\aoc2020\Day5\day5info.txt") as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day5puzzle1(getList()))
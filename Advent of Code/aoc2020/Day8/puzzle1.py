def day8puzzle1(instructions:list):
    ind = 0
    acc = 0
    logs = set()
    NopOrJmp = []
    #add the position where are nop or jmp
    for i in range(len(instructions)):
        if instructions[i][0] == "n" or instructions[i][0] == "j":
            NopOrJmp.append(i)

    for nOjInd in NopOrJmp:
        if instructions[nOjInd][0] == "n":
            instructions[nOjInd] = "jmp "+instructions[nOjInd][4:]
        else:
            instructions[nOjInd] = "nop "+instructions[nOjInd][4:]
        ind = 0
        acc = 0
        while True:
            if ind in logs:
                if instructions[nOjInd][0] == "n":
                    instructions[nOjInd] = "jmp "+instructions[nOjInd][4:]
                else:
                    instructions[nOjInd] = "nop "+instructions[nOjInd][4:]

                logs.clear()
                break
            if ind == len(instructions)-1:
                return acc
            
            logs.add(ind)
            if instructions[ind][0:3] == "nop":
                ind += 1
            elif instructions[ind][0:3] == "acc":
                acc += int(instructions[ind][4:])
                ind += 1
            elif instructions[ind][0:3] == "jmp":
                ind += int(instructions[ind][4:])
            
        

def getList(nameFile:str):
    with open("Advent of Code\\aoc2020\Day8\\"+nameFile) as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day8puzzle1(getList("day8info.txt")))
def getloopSize(publicKey:int):
    loopSize = 0
    subNum = 7
    value = 1
    while value != publicKey:
        value *= subNum
        value %= 20201227
        loopSize += 1
    return loopSize

def getSecretKey(subNum:int, loopSize:int):
    value = 1
    for i in range(loopSize):
        value *= subNum
        value %= 20201227
    return value

# print(getloopSize(5764801)) #card
# print(getloopSize(17807724)) #door

# print(getSecretKey(17807724, 8))



print(getloopSize(13135480)) # card
print(getloopSize(8821721)) # door

#print the result
print(getSecretKey(13135480, 1770247))

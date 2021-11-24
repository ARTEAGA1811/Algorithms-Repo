# https://leetcode.com/problems/decode-ways/
#************************************************************
def getPossibleCombination(chain: str, maxIndex: int, curIndex: int, mysubString: str, logs: dict) -> int:
    # BASE CASES
    if curIndex in logs:
        return logs[curIndex]
    if mysubString[0] == '0' or int(mysubString) > 26:
        return 0
    if curIndex == maxIndex:
        return 1
    
    # RECURSIVE CASES:
    valor = getPossibleCombination(chain, maxIndex, curIndex+1, chain[curIndex+1], logs)
    if curIndex != maxIndex-1:  # to solve the problem of the chain's limit
        valor += getPossibleCombination(chain, maxIndex, curIndex+2, chain[curIndex+1]+chain[curIndex+2], logs)
    #I save the curIndex's value to avoid doing other repeated calculations.
    logs[curIndex] = valor                           
    return valor

def solucionar(s: str):
    chain_size = len(s)
    maxInd = chain_size-1
    logs = {}    
    if chain_size == 0:
        return 0
    if chain_size == 1:
        return getPossibleCombination(s, maxInd, 0, s[0], logs)
    return getPossibleCombination(s, maxInd, 0, s[0], logs) + getPossibleCombination(s, maxInd, 1, s[0] + s[1], logs)


def testCode():
    casosPrueba = [
        '1220125',
        '11106',
        '12',
        '226',
        '0',
        '06',
        '1220125',
        '121',
        '27'
    ]

    salidas = [
        6,2, 2, 3, 0, 0, 6,3,1
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testCode()

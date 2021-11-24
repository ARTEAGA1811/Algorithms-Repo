def solucionar(s:str):
    stack = []
    closeStr = {')',']','}'}
    openStr = {'(','[','{'}
    completeLog = {')':'(',']':'[','}':'{'}
    for i in s:
        if len(stack) == 0:
            if i in closeStr:
                return False
        if i in openStr:
            stack.append(i)
        else:
            if stack[-1] == completeLog[i]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]

    salidas = [
        True,
        True,
        False,
        False,
        True

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()
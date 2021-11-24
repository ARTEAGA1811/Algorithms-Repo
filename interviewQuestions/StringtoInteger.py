#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

def solucionar(s:str):
    s = s.lstrip()
    aux = ''
    if len(s) == 0:
        return 0
    if s[0] == '-' or s[0] == '+':
        if len(s) == 1:
            return 0
        aux+=s[0]
        if not s[1].isnumeric():
            return 0

    else:
        if not s[0].isnumeric():
            return 0
        else:
            aux+=s[0]
            if len(s) == 1:
                return int(s[0])
    
    i = 1
    while i<len(s):
        if s[i].isnumeric():
            aux+=s[i]
            i+=1
        else:
            break

    aux = int(aux)
    if aux>=-2**31 and aux<=(2**31)-1:
        return int(aux)
    else:
        if aux<0:
            return -2**31
        else:
            return (2**31)-1



    
    


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "+1"
    ]

    salidas = [
        42,
        -42,
        4193,
        0,
        -2147483648,
        1
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
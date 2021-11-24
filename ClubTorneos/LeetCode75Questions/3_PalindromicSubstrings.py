#https://leetcode.com/problems/palindromic-substrings/
def myFunction(s:str):
    total = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1]:
                total += 1
    return total



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        "abc",
        "aaa"
    ]

    salidas = [
        3,
        6
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = myFunction(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()
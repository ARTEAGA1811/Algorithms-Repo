#https://leetcode.com/problems/relative-ranks/

def solucionar(score:list):
    auxScore = score.copy()
    auxScore.sort(reverse=True)
    mydic = {}
    for i in enumerate(auxScore):
        mydic[i[1]] = str(i[0]+1)
        if i[0] == 0:
            mydic[i[1]] = "Gold Medal"
        elif i[0] == 1:
            mydic[i[1]] = "Silver Medal"
        elif i[0] == 2:
            mydic[i[1]] = "Bronze Medal"

    for i in range(len(score)):
        score[i] = mydic[score[i]]
    return score


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [5,4,3,2,1],
        [10,3,8,9,4]
    ]

    salidas = [
        ["Gold Medal","Silver Medal","Bronze Medal","4","5"],
        ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

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
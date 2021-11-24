#https://leetcode.com/problems/keyboard-row/
def solucionar(words:list):
    set1 = {'q','w','e','r','t','y','u','i','o','p'}
    set2 = {'a','s','d','f','g','h','j','k','l'}
    set3 = {'z','x','c','v','b','n','m'}
    result = []
    for word in words:
        if set1.intersection(set(word.lower())) == set(word.lower()) or set2.intersection(set(word.lower())) == set(word.lower()) or set3.intersection(word.lower()) == set(word.lower()):
            result.append(word)
    return result
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ["Hello","Alaska","Dad","Peace"],
        ["omk"],
        ["adsdf","sfd"]
    ]

    salidas = [
        ["Alaska","Dad"],
        [],
        ["adsdf","sfd"]

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
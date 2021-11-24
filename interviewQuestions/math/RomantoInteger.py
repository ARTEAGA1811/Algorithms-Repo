#https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
#rango 1-3999
def getSumAum(numEntr:int,chain:str):
    log = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    log2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    if numEntr == 3:
        return log[chain]*3
    if numEntr == 2:
        return log2[chain]
    if numEntr == 1:
        return log[chain]
    
def solucionar(s:str):
    indSel = 0
    mynum = 0
    valids = {'IV','IX','XL','XC','CD','CM'}
    while indSel<=len(s)-1:
        #pruebo los 3.
        if indSel+2<len(s):
            if s[indSel] == s[indSel+1] and s[indSel+1] == s[indSel+2]:
                mynum+=getSumAum(3,s[indSel])
                indSel+=3
                continue
        if indSel+1<len(s):
            if s[indSel]+s[indSel+1] in valids:
                mynum+=getSumAum(2,s[indSel]+s[indSel+1])
                indSel+=2
                continue
        mynum+=getSumAum(1,s[indSel])
        indSel+=1

    return mynum
        


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV",
        'MMMCMXCIX'
    ]

    salidas = [
        3,
        4,
        9,
        58,
        1994,
        3999
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
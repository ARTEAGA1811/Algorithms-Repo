#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
import itertools

#[7, 1, 5, 3, 6, 4]
# compro a 7 y vendo a uno, no me conviene, paso
#compro a 1 y vendo a 5, si, ya gane 4
#compro a 5 y y vendo a 3, no me conviene, paso. (pero hasta ahora ya llevo 4 ganados.)
#y asii.

def solucionar(prices: list):
    # profit = 0
    # for i in range(2,len(prices)+1,2):
    #     aux = list(itertools.combinations(prices,i))
    #     for k in aux:
    #         sumAux = 0
    #         for j in range(len(k)):            
    #             if j%2==0:
    #                 sumAux-=k[j]
    #             else:
    #                 sumAux+=k[j]

    #         if sumAux>profit:
    #             profit = sumAux    
    #     #print(aux)
    # return profit

    #solucionar optimizada, WOW
    maxProfit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            maxProfit+=prices[i]-prices[i-1]
    return maxProfit






class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [7,1,5,3,6,4],
        [1,2,3,4,5],
        [7,6,4,3,1],
        [7,1,5,11,0,20,3,6]
    ]

    salidas = [
        7,4,0,22
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
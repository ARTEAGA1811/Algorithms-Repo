#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
def solucionar(nums:list):
    if len(nums) == 1:
        return nums[0]
    logs = {len(nums)-1:nums[-1],len(nums)-2:nums[-2]}
    def dfs(ind):
        #base case
        if ind in logs:
            return logs[ind]
        #recursive case;
        bestWay = 0
        for i in range(ind+2,len(nums)):
            aux = dfs(i)
            if aux >bestWay:
                bestWay = aux
        bestWay+=nums[ind]
        logs[ind] = bestWay
        return bestWay
    besto = []
    for k in range(0,2):
        besto.append(dfs(k))
    return max(besto)



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [1,2,3,1],
        [2,7,9,3,1],
        [2,1,1,2],
        [1,2,3,4,5,6,7]
    ]

    salidas = [
        4,12,4,16
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
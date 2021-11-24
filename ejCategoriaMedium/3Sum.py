#https://leetcode.com/problems/3sum/
import itertools
def solucionar(nums:list):
    myListCom = list(itertools.combinations(nums,3))
    #print(myListCom)
    valids = []
    for i in myListCom:
        if sum(i) == 0:
            aux = list(i)
            aux.sort()
            valids.append(aux)
    
    #drop duplicates
    valids = list(set(tuple(x) for x in valids))
    valids = [list(x) for x in valids]
    return valids
    
def newSolution(nums:list):
    if len(nums) < 3:
        return []
    checked = []
    valids = []
    for i in range(0,len(nums)):
        if nums[i] not in checked:
            for j in range(i+1,len(nums)):
                if (nums[i],nums[j]) not in checked:
                    for k in range(j+1,len(nums)):
                        if nums[i]+nums[j]+nums[k] == 0:
                            if (nums[i],nums[j]) and (nums[i],nums[k]) and (nums[j],nums[k]) not in checked:
                                valids.append([nums[i],nums[j],nums[k]])
                    checked.append((nums[i],nums[j]))
                    checked.append((nums[j],nums[i]))
            checked.append(nums[i])

    return valids



    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [-1,0,1,2,-1,-4],
        [],
        [0],
        [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]
    ]

    salidas = [
        [[-1,-1,2],[-1,0,1]],
        [],
        [],
        [[1]]

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = newSolution(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()

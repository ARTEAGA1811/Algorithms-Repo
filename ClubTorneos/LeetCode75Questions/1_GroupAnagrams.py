#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def myFunction(strs: list):
    # this algorithm doesn't work for some cases.
    listWithSet = [set(i) for i in strs]
    finalList = []
    for i in range(len(listWithSet)):
        found = False
        for j in range(len(finalList)):
            if listWithSet[i] == listWithSet[finalList[j][0]]:
                finalList[j].append(i)
                found = True
                break  
        if not found:
            finalList.append([i])

    for i in range(len(finalList)):
        for j in range(len(finalList[i])):
            finalList[i][j] = strs[finalList[i][j]]
    return finalList


def myFunctionOptimized(strs:list):
    res = defaultdict(list) #si no encuentra el key lo crea, en este caso como una lista vacia.
    for s in strs:
        count = [0] * 26 #a ... z
        for c in s:
            count[ord(c) - ord('a')] += 1       
        res[tuple(count)].append(s)

    return list(res.values())







class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],       
        ["ddddddddddg","dgggggggggg"]
    ]

    salidas = [
        [["bat"],["nat","tan"],["ate","eat","tea"]],
        [[""]],
        [["a"]],
        [["dgggggggggg"],["ddddddddddg"]]

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = myFunctionOptimized(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()
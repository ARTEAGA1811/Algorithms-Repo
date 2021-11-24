#https://csacademy.com/ieeextreme-practice/task/96c8b1313edd72abf600facb0a14dbab/

# def myFunction(li:list):
#     t = li[0]
#     aux = []
#     for x in range(1,t+1):
#         if li[x] == 1:
#             aux.append(1)
#             continue
#         logs = {li[x]: 1}
#         def dfs(i):
#             if i in logs:
#                 return logs[i]
#             res = dfs(i+1)
#             if i+2<li[x]:
#                 res+=dfs(i+2)
#             logs[i] = res
#             return res
        
#         aux.append(dfs(0)+dfs(1))
#     return aux


def myFunction(li:list):
    t = li[0]
    aux = []
    for x in range(1,t+1):
        if li[x] == 1 or li[x] == 2:
            aux.append(li[x])
            continue
        
        valueOne = 2
        valueTwo = 1
        myvalue = 3
        for i in range(3,li[x]+1):
            myvalue = valueOne+valueTwo
            valueTwo = valueOne
            valueOne = myvalue
        aux.append(myvalue) 
    
    return aux

        



def testCode():
    testCases = [
        [2,1,5],
        [1,2],
        [1,3],
        [1,4],
        [1,5],
        [1,6],
        [1,7],
        [1,8],
        [1,9],
        [1,2]
    ]

    expectedResults = [
        [1,1],
        [2],
        [3],
        [8],
        [9],
        [10],
        [1],
        [10],
        [1],
        [3]

    ]

    for i in range(len(testCases)):
        solution = None
        try:
            solution = myFunction(testCases[i])
            assert solution == expectedResults[i]
            print(
                f"respuesta correcta: test {testCases[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {testCases[i]}, expected {expectedResults[i]}, calculated {solution}", error)

testCode()
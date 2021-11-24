#https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

def solucionar(arr):
    if len(arr) == 1:
        return [-1]
    for i in range(0,len(arr)-1):
        maxNum = max(arr[i+1:])
        arr[i] = maxNum
    arr[-1] = -1
    return arr

print(solucionar([400]))
print(solucionar([17,18,5,4,6,1]))



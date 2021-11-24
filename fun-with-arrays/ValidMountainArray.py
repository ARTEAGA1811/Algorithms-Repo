#https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

def solucionar(arr:list):
    if len(arr)<3:
        return False
    if arr[1] <= arr[0]:
        return False
    change = False
    indChange = 0
    for i in range(2,len(arr)):
        if arr[i]<arr[i-1]:
            change = True
            indChange = i
            break
        elif(arr[i] == arr[i-1]):
            return False
    if not change:
        return False
    if indChange == len(arr)-1:
        return True
    
    for k in range(indChange+1, len(arr)):
        if arr[k] >= arr[k-1]:
            return False
    return True

print(solucionar([2,1]))
print(solucionar([3,5,5]))
print(solucionar([0,3,2,1]))
print(solucionar([9,8,7,6,5,4,3,2,1,0]))    




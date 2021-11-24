#https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/

def solucionar(nums:list):
    aux1 = set(nums)
    aux2 = {x for x in range(1,len(nums)+1)}
    print(aux1)
    print(aux2)
    return list(aux2-aux1)


print(solucionar([4,3,2,7,8,2,3,1]))
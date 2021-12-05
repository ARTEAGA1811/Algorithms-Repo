#https://leetcode.com/problems/climbing-stairs/

def climbingStairs(n: int):
    #it's a fibonacci sequence
    if n == 1:
        return 1
    if n == 2:
        return 2
    v1 = 1
    v2 = 2
    aux = 0
    for i in range(2,n):
        aux = v1+v2
        v1 = v2
        v2 = aux
    return aux
            


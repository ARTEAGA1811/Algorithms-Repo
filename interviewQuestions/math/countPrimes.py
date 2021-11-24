#https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
import math
import re

def solucionar(n:int):
    if n == 0 or n == 1 or n == 2:
        return 0
    aux = [2]
    for i in range(3,n,2):
        flag = True
        for k in aux:
            if int(i/k)>k:
                if i%k==0:
                    flag = False
                    break
            else:
                if i%k==0:
                    flag = False
                break
        if flag:
            aux.append(i)
    #print(aux)
    return len(aux)


def isPrime(n):
    if n == 2:
        return True
    if n<2 or n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True


# def solucionar(n:int):
#     cont = 0
#     for i in range(n):
#         if isPrime(i):
#             cont+=1
#     return cont



        




print(solucionar(50))
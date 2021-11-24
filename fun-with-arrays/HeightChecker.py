#https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

def solucionar(heights:list):
    expected = heights.copy()
    expected.sort()
    cont=0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            cont+=1
    return cont    


print(solucionar([1,1,4,2,1,3]))
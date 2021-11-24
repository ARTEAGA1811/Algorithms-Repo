#https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
def solucionar(arr:list):
    for i in range(len(arr)):
        if(arr[i]%2==0):
            if(arr[i] !=0):
                if arr[i]/2 in arr:
                    return True
            else:
                if 0 in (arr[:i]+arr[i+1:]):
                    return True           
    return False
        
print(solucionar([-2,0,10,-19,4,6,-8]))
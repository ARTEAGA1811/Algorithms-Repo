def getReverse(x:int):
    flag = False
    if x<0:
        x=x*-1
        flag = True 
    xStr = str(x)
    xStr = xStr[::-1]
    x = int(xStr)
    if flag:
        x = x*-1   
    if x>=(-2**31) and x<=((2**31)-1):
        return x
    return 0
     


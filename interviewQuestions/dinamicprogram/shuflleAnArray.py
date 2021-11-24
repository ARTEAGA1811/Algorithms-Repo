import random
class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.logs = []
        

    def reset(self) -> list[int]:
        for i in reversed(self.logs):
            self.changeIndexes(i[0],i[1],self.nums)
        self.logs.clear()
        return self.nums
        

    def shuffle(self) -> list[int]:
        randUno = random.randint(0,len(self.nums)-1)
        randDos = random.randint(0,len(self.nums)-1)
        self.logs.append((randUno,randDos))
        self.changeIndexes(randUno,randDos,self.nums)
        return self.nums

    def changeIndexes(self,num1:int,num2:int,arr:list):
        aux = arr[num1]
        arr[num1] = arr[num2]
        arr[num2] = aux

def main():
    myobj = Solution([1,2,3,4])
    print(myobj.shuffle())
    print(myobj.shuffle())
    print(myobj.shuffle())
    print(myobj.shuffle())
    print(myobj.shuffle())
    print(myobj.reset())
    print(myobj.shuffle())
    print(myobj.shuffle())
    print(myobj.reset())


main()

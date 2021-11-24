def getContainsDuplicateII(nums:list,k:int)->bool:
    mydic = {}
    for i in range(len(nums)):
        if nums[i] in mydic:
            if i<=mydic[nums[i]]:
                return True
            mydic[nums[i]] = k+i
        else:
            mydic[nums[i]] = k+i
    return False

myTest = [
    [
        [1,2,3,1],3
    ],
    [
        [1,0,1,1],1
    ],
    [
        [1,2,3,1,2,3],2
    ]
]

for i in range(len(myTest)):
    print(getContainsDuplicateII(myTest[i][0],myTest[i][1]))
class Bag:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, num,child):
        self.children.append((num,child))
    
    def add_parent(self,parent):
        self.parents.append(parent)

    def get_total_bags(self):
        total = 1
        for child in self.children:
            total += child[0]
        return total

    def __str__(self):
        allString = self.name + ": " + str(self.children) + " " + str(self.parents)
        return allString


def day7puzzle1(arr:list):
    bagList = []
    def getIndBag(nameBag: str):
        for bag in range(len(bagList)):
            if bagList[bag].name == nameBag:
                return bag
        return -1

    for line in arr:
        line = line.split(" bags contain ")
        indBag = getIndBag(line[0])
        if indBag == -1:
            bagList.append(Bag(line[0]))
            indBag = len(bagList)-1
        
        if line[1] != "no other bags.":
            line = line[1].split(", ")
            for item in line:
                item = item.split(" ") #["2","clear","lavender","bags"]
                bagList[indBag].add_child(int(item[0]),item[1]+" "+item[2]) #(2, clear lavender)

                #now I must add the parent to the child
                indChild = getIndBag(item[1]+" "+item[2])
                if indChild == -1:
                    bagList.append(Bag(item[1]+" "+item[2]))
                    indChild = len(bagList)-1
                bagList[indChild].add_parent(bagList[indBag].name)

        
    def getNumBagsPossibles(num:int,nameBag:str):
        indBag = getIndBag(nameBag)
        myChildren = bagList[indBag].children
        #base case
        if len(myChildren) == 0:
            return num
        #recursive case
        total = num
        for child in myChildren:
            total += child[0]*getNumBagsPossibles(num,child[1])
        return total


    numberss = getNumBagsPossibles(1,"shiny gold")
    return numberss-1

def getList(nameFile:str):
    with open("Advent of Code\\aoc2020\Day7\\"+nameFile) as f:
        return [str(line.strip()) for line in f]

#print the answer
print(day7puzzle1(getList("day7info.txt")))
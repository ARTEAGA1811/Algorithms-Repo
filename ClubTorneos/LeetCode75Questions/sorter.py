import random
class MyFile:
    def __init__(self, filePath):
        self.filePath = filePath
    
    def getRandomLink(self):
        miFichero = open(self.filePath, "r")
        exercicesList = miFichero.readlines()
        for i in range(len(exercicesList)):
            exercicesList[i] = exercicesList[i].rstrip("\n")
        #select random value from exercicesList
        miFichero.close()
        randomIndex = random.randint(0, len(exercicesList)-1)
        print(exercicesList[randomIndex])

    def deleteLink(self, link: str):
        with open(self.filePath, "r") as f:
            lines = f.readlines()
        with open(self.filePath, "w") as f:
            for line in lines:
                if line.strip("\n") != link:
                    f.write(line)
                else:
                    print("Link deleted")
    

def main():
    myfile = MyFile("ClubTorneos\LeetCode75Questions\listaEjercicios.txt")
    option = int(input("1-> Get random link\n2-> Delete Link\n"))
    if option == 1:
        myfile.getRandomLink()
    elif option == 2:
        link = input("Link to delete: ")
        myfile.deleteLink(link)

    
main()


    

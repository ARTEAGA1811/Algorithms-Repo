class BrowserHistory:

    def __init__(self, homepage: str):
        self.historyList =[homepage]
        self.curIndex = 0
        

    def visit(self, url: str) -> None:
        for i in range(len(self.historyList)-1,self.curIndex,-1):
            self.historyList.pop(i)
        #self.historyList.insert(self.curIndex+1, url)
        self.historyList.append(url)
        self.curIndex +=1
        

    def back(self, steps: int) -> str:
        if self.curIndex - steps < 0:
            self.curIndex = 0
            return self.historyList[self.curIndex]
        else:
            self.curIndex -=steps
            return self.historyList[self.curIndex]
        

    def forward(self, steps: int) -> str:
        if self.curIndex + steps < len(self.historyList):
            self.curIndex+=steps
            return self.historyList[self.curIndex]
        else:
            self.curIndex = len(self.historyList)-1
            return self.historyList[self.curIndex]

def solucionar():
    pass

def testCode():
    casosPrueba = [
        [
            [2,5,1,3,4,7],
            3
        ],
        [
            [1,2,3,4,4,3,2,1],
            4
        ]

        
    ]

    salidas = [
        [2,3,5,4,1,7],
        [1,4,2,3,3,2,4,1]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testCode()
class Robot:
    def __init__(self) -> None:
        self.carretUp:str="^"
        self.carretRight:str=">"
        self.carretLeft:str="<"
        self.carretDown:str="v"
    
    def __init__(self, currentCarret:str, positionX:int, positionY:int) -> None:
        self.carretUp:str="^"
        self.carretRight:str=">"
        self.carretLeft:str="<"
        self.carretDown:str="v"
        self.currentCarret:str = currentCarret
        self.x:int = positionX
        self.y:int = positionY

    def advancePlus1(self):
        if self.currentCarret == self.carretDown:
            self.y+=1
        elif self.currentCarret == self.carretRight:
            self.x+=1
        elif self.currentCarret == self.carretLeft:
            self.x-=1
        else:
            self.y-=1
        return self.x, self.y
    
    def advanceMinus1(self):
        if self.currentCarret == self.carretDown:
            self.y-=1
        elif self.currentCarret == self.carretRight:
            self.x-=1
        elif self.currentCarret == self.carretLeft:
            self.x+=1
        else:
            self.y+=1
        return self.x, self.y

    def rotatePlus90(self):
        if self.currentCarret == self.carretDown:
            self.currentCarret = self.carretRight
        elif self.currentCarret == self.carretRight:
            self.currentCarret = self.carretUp
        elif self.currentCarret == self.carretLeft:
            self.currentCarret = self.carretDown
        else:
            self.currentCarret = self.carretLeft
        return self.currentCarret

    def __str__(self) -> str:
        return f"{self.currentCarret} at ({self.x},{self.y})"
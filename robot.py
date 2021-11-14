class Robot:
    def __init__(self) -> None:
        self.carretUp="^"
        self.carretRight=">"
        self.carretLeft="<"
        self.carretDown="v"
    
    def __init__(self, currentCarret, positionX, positionY) -> None:
        self.carretUp="^"
        self.carretRight=">"
        self.carretLeft="<"
        self.carretDown="v"
        self.currentCarret = currentCarret
        self.x = positionX
        self.y = positionY

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
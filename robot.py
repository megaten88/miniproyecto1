from mapObject import MapObject
from package import Package
class Robot(MapObject):
    
    def __init__(self, line: int, col: int, carret: str) -> None:
        self.carretUp:str="^"
        self.carretRight:str=">"
        self.carretLeft:str="<"
        self.carretDown:str="v"
        super().__init__(line, col, carret)

    def advancePlus1(self):
        if self.currentCarret == self.carretDown or self.currentCarret==self.carretUp:
            self.line+=1
        elif self.currentCarret == self.carretRight or self.currentCarret == self.carretLeft:
            self.col+=1
        return self.line, self.col
    
    def advanceMinus1(self): 
        if self.currentCarret == self.carretDown or self.currentCarret == self.carretUp:
            self.line-=1
        elif self.currentCarret == self.carretRight or self.currentCarret == self.carretLeft :
            self.col-=1

        return self.line, self.col

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
    
    def rotateMinus90(self):
        if self.currentCarret == self.carretDown:
            self.currentCarret = self.carretLeft
        elif self.currentCarret == self.carretRight:
            self.currentCarret = self.carretDown
        elif self.currentCarret == self.carretLeft:
            self.currentCarret = self.carretUp
        else:
            self.currentCarret = self.carretRight
        return self.currentCarret

    def addPackage(self,pack:Package):
        self.package = pack

    def deliverPackage(self) -> Package:
        deliver = self.package 
        self.package = None
        return deliver

    def __str__(self) -> str:
        return super().__str__()


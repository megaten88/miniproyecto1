class MapObject():
    def __init__(self, x:int, y:int, carret:str) -> None:
        self.x = x
        self.y = y
        self.currentCarret = carret

    def __str__(self) -> str:
        return self.currentCarret
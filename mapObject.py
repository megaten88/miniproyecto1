class MapObject():
    def __init__(self, line:int, col:int, carret:str) -> None:
        self.line = line
        self.col = col
        self.currentCarret = carret
        self.parent:MapObject = None

    def __str__(self) -> str:
        return self.currentCarret
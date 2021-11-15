from mapObject import MapObject

class Destination(MapObject):
    def __init__(self, line: int, col: int, carret: str) -> None:
        super().__init__(line, col, carret)
    
    def __str__(self) -> str:
        return super().__str__()
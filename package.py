from mapObject import MapObject


from mapObject import MapObject

class Package(MapObject):
    def __init__(self, x: int, y: int, carret: str) -> None:
        super().__init__(x, y, carret)
    
    def __str__(self) -> str:
        return super().__str__()
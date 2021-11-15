from robot import Robot
from package import Package
from obstacle import Obstacle
from destination import Destination

class MapTile:
    def __init__(self, lines, columns) -> None:
        self.mapTile = [["-" for x in range(columns)] for y in range (lines)]
        self.packages = []
        self.obs = []
        self.destinations = []
        self.lines = lines
        self.columns = columns
        
    
    def addRobot(self, robot:Robot):
        self.robot = robot
        self.mapTile[robot.x][robot.y] = robot.currentCarret

    def addPackage(self, package:Package):
        self.packages.append(package)
        self.mapTile[package.x][package.y] = package.currentCarret

    def addObstacle(self, obs:Obstacle):
        self.obs.append(obs)
        self.mapTile[obs.x][obs.y] = obs.currentCarret

    def addDestination(self,x:int,y:int, dest:Destination):
        self.destinations.append(dest)
        self.mapTile[x][y] = dest

    def __str__(self) -> str:
        stringMap:str = ""
        for x in range(self.lines):
            for y in range (self.columns):
                if y <self.columns-1:
                    stringMap+= str(self.mapTile[x][y])
                else:
                    stringMap+= str(self.mapTile[x][y])+"\n"
        return stringMap
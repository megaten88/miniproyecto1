from robot import Robot
from package import Package
from obstacle import Obstacle
from destination import Destination

class MapTile:
    def __init__(self, lines, columns) -> None:
        self.mapTile = [["-" for col in range(columns)] for line in range (lines)]
        self.packages = []
        self.obs = []
        self.destinations = []
        self.lines = lines
        self.columns = columns
        
    
    def addRobot(self, robot:Robot):
        self.robot = robot
        self.mapTile[robot.line][robot.col] = robot.currentCarret

    def addPackage(self, package:Package):
        self.packages.append(package)
        self.mapTile[package.line][package.col] = package.currentCarret

    def addObstacle(self, obs:Obstacle):
        self.obs.append(obs)
        self.mapTile[obs.line][obs.col] = obs.currentCarret

    def addDestination(self,line:int,col:int, dest:Destination):
        self.destinations.append(dest)
        self.mapTile[line][col] = dest

    def __str__(self) -> str:
        stringMap:str = ""
        for line in range(self.lines):
            for col in range (self.columns):
                if col <self.columns-1:
                    stringMap+= str(self.mapTile[line][col])
                else:
                    stringMap+= str(self.mapTile[line][col])+"\n"
        return stringMap
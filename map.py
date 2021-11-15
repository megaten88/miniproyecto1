from robot import Robot
from package import Package
from obstacle import Obstacle
from destination import Destination

class Map:
    def __init__(self, lines, columns) -> None:
        self.map = [["-" for x in range(columns)] for y in range (lines)]
        self.packages = []
        self.obs = []
        self.destinations = []
        self.lines = lines
        self.columns = columns
        
    
    def addRobot(self, robot:Robot):
        self.robot = robot
        self.map[robot.x][robot.y] = robot.currentCarret

    def addPackage(self, package:Package):
        self.packages.append(package)
        self.map[package.x][package.y] = package.currentCarret

    def addObstacle(self, obs:Obstacle):
        self.obs.append(obs)
        self.map[obs.x][obs.y] = obs.currentCarret

    def addDestination(self,x:int,y:int, dest:Destination):
        self.destinations.append(dest)
        self.map[x][y] = dest

    def __str__(self) -> str:
        stringMap:str = ""
        for x in range(self.lines):
            for y in range (self.columns):
                if y <self.columns-1:
                    stringMap+= str(self.map[x][y])
                else:
                    stringMap+= str(self.map[x][y])+"\n"
        return stringMap
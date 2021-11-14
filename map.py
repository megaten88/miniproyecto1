from robot import Robot
from package import Package
from obstacle import Obstacle
from prettytable import PrettyTable

class Map:
    def __init__(self, lines, columns) -> None:
        self.map = [["-" for x in range(columns)] for y in range (lines)]
        self.packages = []
        self.obs = []
        
    
    def addRobot(self, robot:Robot):
        self.robot = robot
        self.map[robot.x][robot.y] = robot.currentCarret

    def addPakage(self, package:Package):
        self.packages.append(package)
        self.map[package.x][package.y] = package.carret

    def addObstacle(self, obs:Obstacle):
        self.obs.append(obs)
        self.map[obs.x][obs.y] = obs.carret

    def __str__(self) -> str:
        self.prettyTable:PrettyTable = PrettyTable()
        for line in self.map:
            self.prettyTable.add_row(line)
        print(self.prettyTable)
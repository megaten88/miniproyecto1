import prettytable
from robot import Robot
from prettytable import PrettyTable

class Map:
    def __init__(self, lines, columns, robot:Robot) -> None:
        self.map = [["-" for x in range(columns)] for y in range (lines)]
        self.robot:Robot = robot
        self.map[robot.x][robot.y] = robot.currentCarret
    
    def __str__(self) -> str:
        self.prettyTable:PrettyTable = PrettyTable()
        for line in self.map:
            self.prettyTable.add_row(line)
        print(self.prettyTable)
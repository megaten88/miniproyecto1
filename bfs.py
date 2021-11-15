#!/usr/bin/env python3
'''
Proyecto # 1 

Mayra Salazar
Miguel Flores
'''

import sys
import re
from map import Map
from obstacle import Obstacle
from package import Package
from robot import Robot 

def bfs(map,start, end,): 
    pass

def searchPath():
    pass

def main():
    mapfile = ""
    map:Map = None

    try:
        mapfile = sys.argv[1]
    except IndexError:
        mapfile = None
        print("Elija un mapa válido")

    if mapfile is None:
        sys.exit(1)

    lines = None
    with open(mapfile, 'r+') as  mappingFile:
        lines = mappingFile.readlines()

    count = 0
    for line in lines:
        if count == 0:
            result = re.search(r"(\d*),(\d*)", line)
            map = Map(int(result[1]),int(result[2]))
            count+=1
        else:
            for char in line:
                lns = count-1
                column = line.index(char)
                if char == "D":
                    map.addDestiny(lns,column)
                if char == "O":
                    pack = Package(lns,column)
                    map.addPackage(pack)
                if char == "X":
                    obs = Obstacle(lns,column)
                    map.addObstacle(obs)
                if char in ["<",">","^","v"]:
                    robot = Robot(char,lns,column)
                    map.addRobot(robot)
            count+=1
    print(map)


if __name__ == '__main__':
    main()
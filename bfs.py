#!/usr/bin/env python3
'''
Proyecto # 1 

Mayra Salazar
Miguel Flores
'''

import sys
import re
from map import Map
from mapObject import MapObject
from obstacle import Obstacle
from package import Package
from robot import Robot
from destination import Destination

def bfs(map:Map, start:MapObject, end:MapObject):
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
                    indexes = [index for index, element in enumerate(line) if element == "D"]
                    for inx in indexes:
                        destiny = Destination(lns,inx,"D")
                        map.addDestination(lns,inx)
                if char == "O":
                    indexes = [index for index, element in enumerate(line) if element == "O"]
                    for inx in indexes:
                        pack = Package(lns,inx,"O")
                        map.addPackage(pack)
                if char == "X":
                    indexes = [index for index, element in enumerate(line) if element == "X"]
                    for inx in indexes:
                        obs = Obstacle(lns,inx,"X")
                        map.addObstacle(obs)
                if char in ["<",">","^","v"]:
                    robot = Robot(lns,column,char)
                    map.addRobot(robot)
            count+=1
    print(map)


if __name__ == '__main__':
    main()
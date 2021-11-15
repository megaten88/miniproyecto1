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
from collections import deque as queue

path = []

def bfs(map:Map, start:Robot, end:MapObject):
    frontier:queue = queue()    
    frontier.append((start))
    visited = [(start.x, start.y)]
    while len(frontier) > 0:
        current:Robot = frontier.popleft()
        path.append((current,None))
        if (current.x, current.y) == (end.x,end.y):
            return current

        if current.x+1 < map.lines and map[current.x+1][current.y] == "-":
            parent = current
            map[current.x][current.y] = "-"
            if (current.x,current.y) in visited:
                continue
            if current.currentCarret == ">":
                current.advancePlus1()
            if current.currentCarret == "^":
                current.rotateMinus90()
                current.advancePlus1()
            if current.currentCarret == "<":
                current.rotatePlus90()
                current.rotatePlus90()
                current.advancePlus1()
            if current.currentCarret == "v":
                current.rotatePlus90()
                current.advancePlus1()
            
            current.parent =  parent
            visited.append((current.x, current.y))
            path.append(current)
            frontier.append(current)
            

        
    return None



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
#!/usr/bin/env python3
'''
Proyecto # 1 

Mayra Salazar
Miguel Flores
'''

import sys
import re
from types import coroutine
from mapTiles import  MapTile
from mapObject import MapObject
from obstacle import Obstacle
from package import Package
from robot import Robot
from destination import Destination
from collections import deque as queue

path = []
commands = []

def bfs(mapGraph:MapTile, start:Robot, end:MapObject):
    frontier:queue = queue()    
    frontier.append((start))
    visited = []
    while len(frontier) > 0:
        current:Robot = frontier.popleft()
        path.append((current,None))
        # Validations on Pickup
        if current.x+1 < mapGraph.lines and (current.x+1, current.y) == (end.x,end.y) and end.currentCarret == "O":
            if current.currentCarret == ">":
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "^":
                pass
            elif current.currentCarret == "<":
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "v":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
            package = mapGraph.packages.pop()
            mapGraph.mapTile[package.x][package.y] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current  

        elif current.x-1 >=0 and (current.x-1, current.y) == (end.x,end.y) and end.currentCarret == "O":
            if current.currentCarret == ">":
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "^":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "<":
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "v":
                pass
            package = mapGraph.packages.pop()
            mapGraph.mapTile[package.x][package.y] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current

        elif current.y+1 < mapGraph.columns and (current.x, current.y+1) == (end.x,end.y) and end.currentCarret == "O":
            
            if current.currentCarret == ">":
                pass
            elif current.currentCarret == "^":
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "<":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "v":
                commands.append("rtr    -90")
                current.rotateMinus90()
            package = mapGraph.packages.pop()
            mapGraph.mapTile[package.x][package.y] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current

        elif current.y-1 >= 0 and (current.x, current.y-1) == (end.x,end.y) and end.currentCarret == "O":
            if current.currentCarret == ">": 
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "^":
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "<":
                pass
            elif current.currentCarret == "v":
                commands.append("rtr    +90")
                current.rotatePlus90()
            package = mapGraph.packages.pop()
            mapGraph.mapTile[package.x][package.y] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current
    # ------------Validations on movement------------------ #
        if current.x+1 < mapGraph.lines and mapGraph.mapTile[current.x+1][current.y] != "X":

            parent = current
            mapGraph.mapTile[current.x][current.y] = "-"
            if (current.x,current.y) not in visited:
                visited.append((current.x, current.y))
            else:
                continue

            if current.currentCarret == ">":
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "^":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "<":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "v":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advancePlus1()

        elif current.x-1 >= 0 and mapGraph.mapTile[current.x-1][current.y] != "X":
            parent = current
            mapGraph.mapTile[current.x][current.y] = "-"
            if (current.x,current.y) not in visited:
                visited.append((current.x, current.y))
            else:
                continue

            if current.currentCarret == ">":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "^":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "<":
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "v":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("avz    1")
                current.advanceMinus1()

        elif current.y+1 < mapGraph.columns and mapGraph.mapTile[current.x][current.y+1] != "X":
            parent = current
            mapGraph.mapTile[current.x][current.y] = "-"
            if (current.x,current.y) not in visited:
                visited.append((current.x, current.y))
            else:
                continue
            if current.currentCarret == ">":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "^":
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "<":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("avz    1")
                current.advancePlus1()
            elif current.currentCarret == "v":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advancePlus1()

        elif current.y-1 >= 0 and mapGraph.mapTile[current.x][current.y-1] != "X":

            parent = current
            mapGraph.mapTile[current.x][current.y] = "-"
            if (current.x,current.y) not in visited:
                visited.append((current.x, current.y))
            else:
                continue
            if current.currentCarret == ">":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "^":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "<":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("avz    1")
                current.advanceMinus1()
            elif current.currentCarret == "v":
                commands.append("avz    1")
                current.advanceMinus1()
        print("current", current, current.x, current.y)
        current.parent =  parent
        mapGraph.robot = current
        mapGraph.mapTile[current.x][current.y] = current
        frontier.append(current)
        
            
    return None

def main():
    mapGraphfile = ""
    mapGraphGraph:MapTile = None

    try:
        mapGraphfile = sys.argv[1]
    except IndexError:
        mapGraphfile = None
        print("Elija un mapGrapha válido")

    if mapGraphfile is None:
        sys.exit(1)

    lines = None
    with open(mapGraphfile, 'r+') as  mapGraphpingFile:
        lines = mapGraphpingFile.readlines()

    count = 0
    for line in lines:
        if count == 0:
            result = re.search(r"(\d*),(\d*)", line)
            mapGraphGraph = MapTile(int(result[1]),int(result[2]))
            count+=1
        else:
            for char in line:
                lns = count-1
                column = line.index(char)
                if char == "D":
                    indexes = [index for index, element in enumerate(line) if element == "D"]
                    for inx in indexes:
                        destination = Destination(lns,inx,"D")
                        mapGraphGraph.addDestination(lns,inx,destination)
                if char == "O":
                    indexes = [index for index, element in enumerate(line) if element == "O"]
                    for inx in indexes:
                        pack = Package(lns,inx,"O")
                        mapGraphGraph.addPackage(pack)
                if char == "X":
                    indexes = [index for index, element in enumerate(line) if element == "X"]
                    for inx in indexes:
                        obs = Obstacle(lns,inx,"X")
                        mapGraphGraph.addObstacle(obs)
                if char in ["<",">","^","v"]:
                    robot = Robot(lns,column,char)
                    mapGraphGraph.addRobot(robot)
            count+=1
    print(mapGraphGraph)
    print(bfs(mapGraphGraph, mapGraphGraph.robot, mapGraphGraph.packages[0]))
    print("Robot",mapGraphGraph.robot, mapGraphGraph.robot.y, mapGraphGraph.robot.y)
    print("commands",commands)
    print(mapGraphGraph)


if __name__ == '__main__':
    main()
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
from copy import deepcopy

paths = []
commands = []
visited = []
mapGraphfile = ""
mapGraphGraph:MapTile = None
count = 0
def bfs(mapGraph:MapTile, start:Robot, end:MapObject):
    frontier:queue = queue()  
    start.parent = None  
    frontier.append((start))
    path = []
    while len(frontier) > 0:
        current:Robot = frontier.popleft()
        visited.append((current.line, current.col))
        # Validations on Pickup
        if current.line+1 < mapGraph.lines and (current.line+1, current.col) == (end.line,end.col) and end.currentCarret == "O":
            if current.currentCarret == "<":
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "v":
                pass
            elif current.currentCarret == ">":
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "^":
                commands.append("rtr    -90")
                current.rotateMinus90()
                commands.append("rtr    -90")
                current.rotateMinus90()
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current 
            package = end
            mapGraph.mapTile[package.line][package.col] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current  

        if current.col+1 < mapGraph.columns and (current.line, current.col+1) == (end.line,end.col) and end.currentCarret == "O":
            
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
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            package = end
            mapGraph.mapTile[package.line][package.col] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current

        if current.line-1 >=0 and (current.line-1, current.col) == (end.line,end.col) and end.currentCarret == "O":
            if current.currentCarret == "<":            
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == "v":
                commands.append("rtr    +90")
                current.rotatePlus90()
                commands.append("rtr    +90")
                current.rotatePlus90()
            elif current.currentCarret == ">":
                commands.append("rtr    -90")
                current.rotateMinus90()
            elif current.currentCarret == "^":
                pass
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            package = end
            mapGraph.mapTile[package.line][package.col] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current

        if current.col-1 >= 0 and (current.line, current.col-1) == (end.line,end.col) and end.currentCarret == "O":
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
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            package = end
            mapGraph.mapTile[package.line][package.col] = "-"
            current.addPackage(package)
            commands.append("crg    1")
            return current
####---------------Validations on Movement--------------------####
        availables = searchPaths(mapGraph, current)
        reset_current =  deepcopy(current)
        reset_mapgraph = deepcopy(mapGraph)
        for location in availables:           
            if location in visited:
                continue
            if location == (current.line+1, current.col):# v
                if reset_current.currentCarret == "v":
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == ">":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "^":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "<":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
            elif location == (current.line, current.col+1): # >
                if reset_current.currentCarret == "v":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == ">":
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "^":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "<":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advancePlus1()
            elif location == (current.line-1, current.col):
                if reset_current.currentCarret == "v":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "<":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "^":
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == ">":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
            elif location == (current.line, current.col-1):
                if reset_current.currentCarret == "v":
                    commands.append("rtr    -90")
                    reset_current.rotateMinus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == ">":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "^":
                    commands.append("rtr    +90")
                    reset_current.rotatePlus90()
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "<":
                    commands.append("avz    1")
                    reset_current.advanceMinus1()
            reset_current.parent = current
            print("current", reset_current, reset_current.line, reset_current.col)
            reset_mapgraph.robot = reset_current
            if current!= start and str(reset_mapgraph.mapTile[start.line][start.col]) == ">":
                reset_mapgraph.mapTile[start.line][start.col] = "-"
            reset_mapgraph.mapTile[current.line][current.col] = "-"
            reset_mapgraph.mapTile[reset_current.line][reset_current.col] = reset_current
            print(reset_mapgraph)
            visited.append(location)
            frontier.append(reset_current)
            reset_current =  deepcopy(current)
            reset_mapgraph = deepcopy(mapGraph)
            
    return None

def main():
    
    mapGraphGraph = create_map()
    robot= (bfs(mapGraphGraph, mapGraphGraph.robot, mapGraphGraph.packages[0]))

    # for p in paths:
    #     for i in p:
    #         print(i.currentCarret, i.line, i.col)
    print("Robot",mapGraphGraph.robot, mapGraphGraph.robot.line, mapGraphGraph.robot.col)
    print(mapGraphGraph)


def searchPaths(mapGraph:MapTile,robot:Robot):
    locations = []
    if robot.line+1 < mapGraph.lines and mapGraph.mapTile[robot.line+1][robot.col] != "X":
        locations.append((robot.line+1,robot.col))
    if robot.col+1 < mapGraph.columns and mapGraph.mapTile[robot.line][robot.col+1] != "X":
        locations.append((robot.line,robot.col+1))
    if robot.line-1 >= 0 and mapGraph.mapTile[robot.line-1][robot.col] != "X":
        locations.append((robot.line-1,robot.col))
    if robot.col-1 >= 0 and mapGraph.mapTile[robot.line][robot.col-1] != "X":
        locations.append((robot.line,robot.col-1))
    return locations
        

def create_map():
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
                    print(lns, column, char)
                    robot = Robot(lns,column,char)
                    mapGraphGraph.addRobot(robot)
            count+=1
    return mapGraphGraph

if __name__ == '__main__':
    main()
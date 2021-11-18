#!/usr/bin/env python3
'''
Proyecto # 1 

Mayra Salazar
Miguel Flores
'''

import sys
import re
from timeit import default_timer
from types import coroutine
from mapTiles import  MapTile
from mapObject import MapObject
from obstacle import Obstacle
from package import Package
from robot import Robot
from destination import Destination
from collections import deque as queue
from copy import deepcopy

commands = []
visited = []
mapGraphfile = ""
mapGraphGraph:MapTile = None
count = 0
def bfs(mapGraph:MapTile, start:Robot, end:MapObject):
    frontier:queue = queue()  
    frontier.append((start))
    while len(frontier) > 0:
        current:Robot = frontier.popleft()
        visited.append((current.line, current.col))
        # Validations on Pickup
        if current.line+1 < mapGraph.lines and (current.line+1, current.col) == (end.line,end.col) and (end.currentCarret == "O" or end.currentCarret == "D"):
            if current.currentCarret == "<":
                commands.append((current, current.parent,"rtr    -90","v"))
                current.rotateMinus90()
            elif current.currentCarret == "v":
                pass
            elif current.currentCarret == ">":
                commands.append((current, current.parent,"rtr    +90","v"))
                current.rotatePlus90()
            elif current.currentCarret == "^":
                commands.append((current, current.parent,"rtr    -90","v"))
                current.rotateMinus90()
                commands.append((current, current.parent,"rtr    -90","v"))
                current.rotateMinus90()
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current 
            if end.currentCarret == "O":
                package = end
                mapGraph.mapTile[package.line][package.col] = "-"
                current.addPackage(package)
                commands.append((current, current.parent,"crg    1","pk"))
            else:
                package = end
                mapGraph.mapTile[package.line][package.col] = "C"
                current.deliverPackage()
                commands.append((current, current.parent,"crg    0","pk"))
            return current  

        if current.col+1 < mapGraph.columns and (current.line, current.col+1) == (end.line,end.col) and (end.currentCarret == "O" or end.currentCarret == "D"):
            
            if current.currentCarret == ">":
                pass
            elif current.currentCarret == "^":
                commands.append((current, current.parent,"rtr    +90",">"))
                current.rotatePlus90()
            elif current.currentCarret == "<":
                commands.append((current, current.parent,"rtr    -90",">"))
                current.rotateMinus90()
                commands.append((current, current.parent,"rtr    -90",">"))
                current.rotateMinus90()
            elif current.currentCarret == "v":
                commands.append((current, current.parent,"rtr    -90",">"))
                current.rotateMinus90()
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            if end.currentCarret == "O":
                package = end
                mapGraph.mapTile[package.line][package.col] = "-"
                current.addPackage(package)
                commands.append((current, current.parent,"crg    1","pk"))
            else:
                package = end
                mapGraph.mapTile[package.line][package.col] = "C"
                current.deliverPackage()
                commands.append((current, current.parent,"crg    0","pk"))
            return current

        if current.line-1 >=0 and (current.line-1, current.col) == (end.line,end.col) and (end.currentCarret == "O" or end.currentCarret == "D"):
            if current.currentCarret == "<":            
                commands.append((current, current.parent,"rtr    +90","^"))
                current.rotatePlus90()
            elif current.currentCarret == "v":
                commands.append((current, current.parent,"rtr    +90","^"))
                current.rotatePlus90()
                commands.append((current, current.parent,"rtr    +90","^"))
                current.rotatePlus90()
            elif current.currentCarret == ">":
                commands.append((current, current.parent,"rtr    -90","^"))
                current.rotateMinus90()
            elif current.currentCarret == "^":
                pass
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            if end.currentCarret == "O":
                package = end
                mapGraph.mapTile[package.line][package.col] = "-"
                current.addPackage(package)
                commands.append((current, current.parent,"crg    1","pk"))
            else:
                package = end
                mapGraph.mapTile[package.line][package.col] = "C"
                current.deliverPackage()
                commands.append((current, current.parent,"crg    0","pk"))
            return current

        if current.col-1 >= 0 and (current.line, current.col-1) == (end.line,end.col) and (end.currentCarret == "O" or end.currentCarret == "D"):
            if current.currentCarret == ">": 
                commands.append((current, current.parent,"rtr    -90","<"))
                current.rotateMinus90()
                commands.append((current, current.parent,"rtr    -90","<"))
                current.rotateMinus90()
            elif current.currentCarret == "^":
                commands.append((current, current.parent,"rtr    -90","<"))
                current.rotateMinus90()
            elif current.currentCarret == "<":
                pass
            elif current.currentCarret == "v":
                commands.append((current, current.parent,"rtr    +90","<"))
                current.rotatePlus90()
            mapGraph.mapTile[start.line][start.col] = "-"
            mapGraph.robot = current
            mapGraph.mapTile[current.line][current.col] = current
            if end.currentCarret == "O":
                package = end
                mapGraph.mapTile[package.line][package.col] = "-"
                current.addPackage(package)
                commands.append((current, current.parent,"crg    1","pk"))
            else:
                package = end
                mapGraph.mapTile[package.line][package.col] = "C"
                current.deliverPackage()
                commands.append((current, current.parent,"crg    0","pk"))
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
                    commands.append((reset_current, current,"avz    1","v"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == ">":
                    commands.append((reset_current, current,"rtr    -90","v"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1","v"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "^":
                    commands.append((reset_current, current,"rtr    +90","v"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"rtr    +90","v"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1", "v"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "<":
                    commands.append((reset_current, current,"rtr    +90","v"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1","v"))
                    reset_current.advancePlus1()
            elif location == (current.line, current.col+1): # >
                if reset_current.currentCarret == "v":
                    commands.append((reset_current, current,"rtr    +90",">"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1",">"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == ">":
                    commands.append((reset_current, current,"avz    1",">"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "^":
                    commands.append((reset_current, current,"rtr    -90",">"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1", ">"))
                    reset_current.advancePlus1()
                elif reset_current.currentCarret == "<":
                    commands.append((reset_current, current,"rtr    -90", ">"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"rtr    -90",">"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1",">"))
                    reset_current.advancePlus1()
            elif location == (current.line-1, current.col):
                if reset_current.currentCarret == "v":
                    commands.append((reset_current, current,"rtr    -90","^"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"rtr    -90","^"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1","^"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "<":
                    commands.append((reset_current, current,"rtr    -90","^"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1","^"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "^":
                    commands.append((reset_current, current,"avz    1","^"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == ">":
                    commands.append((reset_current, current,"rtr   +90","^"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1","^"))
                    reset_current.advanceMinus1()
            elif location == (current.line, current.col-1):
                if reset_current.currentCarret == "v":
                    commands.append((reset_current, current,"rtr    -90","<"))
                    reset_current.rotateMinus90()
                    commands.append((reset_current, current,"avz    1","<"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == ">":
                    commands.append((reset_current, current,"rtr    +90","<"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"rtr    +90","<"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1","<"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "^":
                    commands.append((reset_current, current,"rtr    +90","<"))
                    reset_current.rotatePlus90()
                    commands.append((reset_current, current,"avz    1","<"))
                    reset_current.advanceMinus1()
                elif reset_current.currentCarret == "<":
                    commands.append((reset_current, current,"avz    1","<"))
                    reset_current.advanceMinus1()
            reset_current.parent = current
            print("current", reset_current, reset_current.line, reset_current.col)
            reset_mapgraph.robot = reset_current
            if current!= start:
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
    inicio= default_timer()
    mapGraphGraph, file = create_map()
    packages = len(mapGraphGraph.packages)
    solution = ""
    robotDeliver = None
    for i in range(packages):
        robotCharge = (bfs(mapGraphGraph, mapGraphGraph.robot, mapGraphGraph.packages[i]))
        print(mapGraphGraph)
        global visited
        visited = [(robotCharge.line,robotCharge.col)]
        robotDeliver = (bfs(mapGraphGraph, mapGraphGraph.robot, mapGraphGraph.destinations[i]))
        print(mapGraphGraph)
        visited = []
    commands_result = returnPath(robotDeliver)
    solution+="\n".join(commands_result)+"\n"
    

    result = re.search(r"_(\d+)", file)
    resultFile = f"resullt_{result[1]}.txt"
    with open(resultFile,"+w") as deliverResult:
        deliverResult.writelines(solution)
    fin = default_timer()
    print(fin-inicio)    

def searchPaths(mapGraph:MapTile,robot:Robot):
    locations = []
    if robot.line+1 < mapGraph.lines and mapGraph.mapTile[robot.line+1][robot.col] != "X" and mapGraph.mapTile[robot.line+1][robot.col] != "O":
        locations.append((robot.line+1,robot.col))
    if robot.col+1 < mapGraph.columns and mapGraph.mapTile[robot.line][robot.col+1] != "X" and mapGraph.mapTile[robot.line][robot.col+1] != "O":
        locations.append((robot.line,robot.col+1))
    if robot.line-1 >= 0 and mapGraph.mapTile[robot.line-1][robot.col] != "X" and mapGraph.mapTile[robot.line-1][robot.col] != "O":
        locations.append((robot.line-1,robot.col))
    if robot.col-1 >= 0 and mapGraph.mapTile[robot.line][robot.col-1] != "X" and mapGraph.mapTile[robot.line][robot.col-1] != "O":
        locations.append((robot.line,robot.col-1))
    return locations

def returnPath(robot:Robot):
    path = [robot]

    while robot is not None and robot.parent is not None:
        path.append(robot.parent)
        robot = robot.parent
    path.reverse()
    all_sequence = []
    for r in path:
        for command in commands:
            if (command[0] == r and command[1] == r.parent and (command[3] == r.currentCarret or command[3] == "pk")):
                all_sequence.append(command[2])
    return all_sequence



        

def create_map():
    try:
        mapGraphfile = sys.argv[1]
    except IndexError:
        mapGraphfile = None
        print("Elija un mapGrapha válido")

    if mapGraphfile is None:
        sys.exit(1)
    sys.setrecursionlimit(10000)
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
            char_found = []
            for char in line:
                if char in char_found:
                    continue
                lns = count-1
                column = line.index(char)
                if char == "D":
                    indexes = [index for index, element in enumerate(line) if element == "D"]
                    for inx in indexes:
                        destination = Destination(lns,inx,"D")
                        mapGraphGraph.addDestination(lns,inx,destination)
                    char_found.append("D")
                if char == "O":
                    indexes = [index for index, element in enumerate(line) if element == "O"]
                    for inx in indexes:
                        pack = Package(lns,inx,"O")
                        mapGraphGraph.addPackage(pack)
                    char_found.append("O")
                if char == "X":
                    indexes = [index for index, element in enumerate(line) if element == "X"]
                    for inx in indexes:
                        obs = Obstacle(lns,inx,"X")
                        mapGraphGraph.addObstacle(obs)
                    char_found.append("X")
                if char in ["<",">","^","v"]:
                    print(lns, column, char)
                    robot = Robot(lns,column,char)
                    robot.parent = None
                    mapGraphGraph.addRobot(robot)
                    char_found.append(char)
            count+=1
    return (mapGraphGraph, mapGraphfile)

if __name__ == '__main__':
    main()
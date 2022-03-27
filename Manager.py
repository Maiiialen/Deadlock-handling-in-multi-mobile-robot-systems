from Point import Point
from Robot import Robot
from Grid import Grid
from Graph import Graph
import math
import copy
from xml.etree.ElementTree import iselement
import matplotlib.pyplot as plt


class Manager:
    grid: Grid
    robots: list

    def __init__(self, file):
        self.grid, self.robots = self.readConfiguration(file)
        self.shortestPathEuclidean()

    def readConfiguration(file):
        with open(file,'r') as f:
            lines = f.readlines()

        isGrid = False
        isRobot = False
        robots = []
        points = []
        values = []

        for line in lines:
            data = line.split(" ")
            if not isGrid and data[0] == 'g':
                grid = Grid(int(data[1]), int(data[2]), int(data[3]))
                isGrid = True
            elif not isRobot and data[0] == 'r':
                values.append(int(data[1]))
                values.append(int(data[2]))
                values.append(int(data[3]))
                isRobot = True
            elif isRobot and data[0] == 'r':
                robot = Robot(values[0], values[1], values[2], copy.deepcopy(points))
                robots.append(robot)

                points = []
                values = []
                values.append(int(data[1]))
                values.append(int(data[2]))
                values.append(int(data[3]))
            elif isRobot and data[0] == 'd':
                disc = Point(int(data[1]), int(data[2]))
                points.append(disc)
            
        robot = Robot(values[0], values[1], values[2], copy.deepcopy(points))
        robots.append(robot)
        
        if isGrid and len(robots) > 0:
            # print("Grid")
            # grid.printGrid()
            # for robot in robots:
            #     robot.printRobot()
            return grid, robots
        else:
            print("not given grid or robots!")
            return 0, 0

    def EuclideanAlgorithm(self, point1, point2):   # TO DO end-point liczyć do krawędzi i jako 1 punkt będzie pozycja robota więc to też trzeba liczyć
        return math.sqrt(math.pow(point1.x - point2.x, 2) + math.pow(point1.y - point2.y, 2))

    def ManhattanAlgorithm(self, point1, point2):   # TO DO end-point liczyć do krawędzi i jako 1 punkt będzie pozycja robota więc to też trzeba liczyć
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    def findClosestEdge(self, point):               # TO DO tu policzyć odległości do krawędzi i zwrócić punkt, gdzie jest najkrótsze
        pass
            

    def shortestPathEuclidean(self):
        for robot in self.robots:
            path = []
            path.append(Point(robot.position_x, robot.position_y))
            path += robot.path
            for point in robot.path:
                end = self.findClosestEdge(point)
                path.append(end)
            graph = Graph(len(path))
            for point1 in range(0, len(path)):
                for point2 in range(point1+1, len(path)):
                    value = self.EuclideanAlgorithm(path[point1], path[point2])
                    graph.add_edge(point1, point2, value)
                    graph.add_edge(point2, point1, value)
            D = graph.dijkstra(0)
            print(D[len(path)-1])
            robot.path = path

    def shortestPathManhattan(self):
        pass
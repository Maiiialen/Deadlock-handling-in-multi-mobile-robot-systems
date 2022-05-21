from re import I, S
from turtle import delay
from Point import Point
from Robot import Robot
from Grid import Grid
import math
import copy
from xml.etree.ElementTree import iselement
import matplotlib.pyplot as plt
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import matplotlib
from matplotlib import pyplot as plt, patches
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy
import random
import numpy as np

class Manager_goSide:
    grid: Grid
    robots: list
    colors: list
    cell_capacity: int
    method: int
    resources_management:int
    blocked = 0
    ended = 0

    def __init__(self, file, cell_capacity, method, resources_management):
        self.cell_capacity = cell_capacity
        self.method = method
        self.resources_management = resources_management
        self.grid, self.robots = self.readConfiguration(file)
        self.addRobotsToGrid()
        self.findShortestPath()
        # self.colorsGenerator()



    def readConfiguration(self, file):
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
                grid = Grid(int(data[1]), int(data[2]), int(data[3]), self.cell_capacity)
                isGrid = True
            elif not isRobot and data[0] == 'r':
                values.append(int(data[1]))
                values.append(int(data[2]))
                values.append(int(data[3]))
                values.append(int(data[4]))
                isRobot = True
            elif isRobot and data[0] == 'r':
                robot = Robot(values[0], values[1], values[2], values[3], copy.deepcopy(points))
                robots.append(robot)

                points = []
                values = []
                values.append(int(data[1]))
                values.append(int(data[2]))
                values.append(int(data[3]))
                values.append(int(data[4]))
            elif isRobot and data[0] == 'd':
                disc = Point(int(data[1]), int(data[2]))
                points.append(disc)
            
        robot = Robot(values[0], values[1], values[2], values[3], copy.deepcopy(points))
        robots.append(robot)
        
        if isGrid and len(robots) > 0:
            return grid, robots
        else:
            print("not given grid or robots!")
            return 0, 0


    def addRobotsToGrid(self):
        for robot in self.robots:
            self.grid.addRobotPosition(robot, Point(robot.position_x, robot.position_y))

    def findClosestEdge(self, point):
        x_size = self.grid.x_cells*self.grid.cell_size
        y_size = self.grid.y_cells*self.grid.cell_size
        if min(point.x, x_size-point.x) < min(point.y, y_size-point.y):
            if point.x < x_size-point.x:
                x_size = 0
            else:
                x_size = x_size
            y_size = point.y
        else:
            if point.y < y_size-point.y:
                y_size = 0
            else:
                y_size = y_size
            x_size = point.x
        return Point(x_size, y_size)

    def findShortestPath(self):
        """Entry point of the program."""
        # Instantiate the data problem.
        for robot in self.robots:
            data = create_data_model(robot)

            # Create the routing index manager.
            manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                                data['num_vehicles'], data['depot'])

            # Create Routing Model.
            routing = pywrapcp.RoutingModel(manager)

            if self.method == 0:
                distance_matrix = compute_euclidean_distance_matrix(data['locations'])
            else:
                distance_matrix = compute_manhattan_distance_matrix(data['locations'])
            # distance_matrix = compute_manhattan_distance_matrix(data['locations'])
            

            def distance_callback(from_index, to_index):
                """Returns the distance between the two nodes."""
                # Convert from routing variable Index to distance matrix NodeIndex.
                from_node = manager.IndexToNode(from_index)
                to_node = manager.IndexToNode(to_index)
                return distance_matrix[from_node][to_node]

            transit_callback_index = routing.RegisterTransitCallback(distance_callback)

            # Define cost of each arc.
            routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

            # Setting first solution heuristic.
            search_parameters = pywrapcp.DefaultRoutingSearchParameters()
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

            # Solve the problem.
            solution = routing.SolveWithParameters(search_parameters)

            indexes = valuesReturn(manager, routing, solution)
            path = []
            for idx in indexes:
                path.append(Point(data['locations'][idx][0], data['locations'][idx][1]))
            path.append(self.findClosestEdge(path[len(path)-1]))
            # for p in path:
            #     p.printp()
            robot.path = path

    def willNotCollide(self, given_robot, new_point):
        for robot in self.robots:
            if not robot == given_robot:
                if (int(math.hypot((new_point.x - robot.position_x),(new_point.y - robot.position_y)))) < given_robot.size/2 + robot.size/2:
                    return False
        return True
                

    def manage(self):
        # self.print()
        # input()
        numberOfRobots = len(self.robots)
        while True:
            results = self.move()
            if len(self.robots) == 0:
                return str(numberOfRobots) + " 0"
            if results != "ok":
                return results

    def move(self):
        # self.print()
        blocked = 0
        for i, robot in enumerate(self.robots):
            new_point = robot.calculateMove(self.method)
            if len(robot.path) == 0:
                self.grid.removeRobotPosition(robot)
                # self.colors.pop(i)
                self.robots.remove(robot)
                self.ended += 1
            else:
                if self.willNotCollide(robot, new_point) and (self.resources_management == 0 or (self.resources_management == 1 and self.grid.updateRobotPosition(robot, new_point))):
                    robot.move(new_point)
                else:
                    robot.blocked += 1
                    blocked += 1
                    if robot.blocked > numpy.random.randint(5,25):
                        robot.blocked = 0
                        robot.changeSide(self.method, math.floor((random.randint(15, 25)/10) * self.grid.cell_size))
                        robot.isGoingBack = 1
                        if not self.grid.isCorrectPoint(robot):
                            robot.removePoint()
                            robot.isGoingBack = 0
            if robot.sameSizeNumber >= 10:
                self.blocked += 1
        if self.blocked == len(self.robots):
            return str(self.ended) + " " + str(len(self.robots))
        else:
            self.blocked = 0
        return "ok"
        # if blocked == len(self.robots):
        #     self.blocked += 1
        #     if self.blocked >= 1000:
        #         return str(self.ended) + " " + str(len(self.robots))
        # else:
        #     self.blocked = 0
        # return "ok"
    
    def colorsGenerator(self):
        self.colors = []
        for _ in self.robots:
            self.colors.append(numpy.random.rand(3,))

    def print(self):
        plt.clf()
        plt.rcParams["figure.autolayout"] = False
        fig = plt.figure(1)
        fig.set_size_inches(10, 9)
        ax = fig.add_subplot(111)
        plt.autoscale(False, 'both')
        i = 0
        # x = [-1, -1, 11, 11]
        # y = [-1, 11, -1, 11]
        # plt.scatter(x, y)
        major_ticks = np.arange(0, self.grid.x_cells*self.grid.cell_size/2000+self.grid.cell_size/2000, self.grid.x_cells*self.grid.cell_size/2000)
        minor_ticks = np.arange(0, self.grid.y_cells*self.grid.cell_size/2000+self.grid.cell_size/2000, self.grid.y_cells*self.grid.cell_size/2000)
        # major_ticks = np.arange(0, self.grid.x_cells*self.grid.cell_size/2000+self.grid.cell_size/2000, self.grid.cell_size/2000)
        # minor_ticks = np.arange(0, self.grid.y_cells*self.grid.cell_size/2000+self.grid.cell_size/2000, self.grid.cell_size/2000)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
        ax.set_axisbelow(True)
        ax.grid()
        for robot in self.robots:
            ax.add_patch(patches.Circle((robot.position_x/2000, robot.position_y/2000), radius=robot.size/4000, color=self.colors[i]))
            for point in robot.path:
                ax.add_patch(patches.Circle((point.x/2000, point.y/2000), radius=0.05, color=self.colors[i]))
            i += 1
        plt.axis('equal')
        plt.draw()
        plt.pause(0.001)
        
def create_data_model(robot:Robot):
    """Stores the data for the problem."""
    data = {}
    # Locations in block units
    data['locations'] = []
    path = robot.path
    for point1 in path:
       # point1.printp()
        data['locations'].append((point1.x, point1.y))
    # print(data)

    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    first = locations[0]
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                if to_node == first:
                    distances[from_counter][to_counter] = 0
                else:
                    distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def compute_manhattan_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    first = locations[0]
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Manhattan distance
                if to_node == first:
                    distances[from_counter][to_counter] = 0
                else:
                    distances[from_counter][to_counter] = abs(from_node[0] - to_node[0]) + abs(from_node[1] - to_node[1])
    return distances


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def valuesReturn(manager, routing, solution):
    index = routing.Start(0)
    plan_output = []
    while not routing.IsEnd(index):
        plan_output.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    return plan_output



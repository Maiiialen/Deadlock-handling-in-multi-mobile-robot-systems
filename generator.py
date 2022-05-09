import random
import math

from numpy import correlate, greater
from Point import Point
from Grid import Grid
from Robot import Robot

cell_size = 2000
velocity = []
size = []

for _ in range(0, 2000):
    velocity.append(random.randint(100, 500))
    size.append(math.floor((random.randint(5, 8)/10) * cell_size))


def generator(file, gridSize_x, gridSize_y, robotsNumber_percent, discs):
    lines = []

    # grid
    line = "g " + str(gridSize_x) + " " + \
        str(gridSize_y) + " " + str(cell_size)
    lines.append(line)

    grid = Grid(gridSize_x, gridSize_y, cell_size, 1)

    # robots
    robots_number = robotsNumber_percent*gridSize_x*gridSize_y//100
    for i in range(0, robots_number):
        # print(robots_number)
        robot_size = size[i]
        robot_velocity = velocity[i]
        CorrectPlace = False
        while(not CorrectPlace):
            pos_x = random.randint(
                robot_size//2, gridSize_x*cell_size - robot_size//2)
            pos_y = random.randint(
                robot_size//2, gridSize_y*cell_size - robot_size//2)
            robot = Robot(robot_size, 1, pos_x, pos_y, [])
            CorrectPlace = grid.addRobotPosition(robot, Point(pos_x, pos_y))
        line = "r " + str(robot_size) + " " + str(robot_velocity) + \
            " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = discs
        # disc_number = random.randint(3, 10)
        for _ in range(0, disc_number):
            disc_x = random.randint(
                robot_size//2, gridSize_x*cell_size - robot_size//2)
            disc_y = random.randint(
                robot_size//2, gridSize_y*cell_size - robot_size//2)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)

    with open(file, 'w') as f:
        f.write("")
    for line in lines:
        with open(file, 'a') as f:
            f.write(line)
            f.write("\n")


def generatorCells(file, gridSize_x, gridSize_y, robotsNumber_percent, discs):
    lines = []
    robotPoints = []

    # grid
    line = "g " + str(gridSize_x) + " " + \
        str(gridSize_y) + " " + str(cell_size)
    lines.append(line)

    # robots
    robots_number = robotsNumber_percent*gridSize_x*gridSize_y//100
    for i in range(0, robots_number):
        robot_size = size[i]
        robot_velocity = velocity[i]
        notCorrectPlace = True
        while(notCorrectPlace):
            pos_x = random.randrange(
                cell_size//2, gridSize_x*cell_size - cell_size//2, cell_size)
            pos_y = random.randrange(
                cell_size//2, gridSize_y*cell_size - cell_size//2, cell_size)
            notCorrectPlace = False
            for point in robotPoints:
                if pos_x != point.x and pos_y != point.y:
                    notCorrectPlace = False
        line = "r " + str(robot_size) + " " + str(robot_velocity) + \
            " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = discs
        for _ in range(0, disc_number):
            disc_x = random.randrange(
                cell_size//2, gridSize_x*cell_size - cell_size//2, cell_size)
            disc_y = random.randrange(
                cell_size//2, gridSize_y*cell_size - cell_size//2, cell_size)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)

    with open(file, 'w') as f:
        f.write("")
    for line in lines:
        with open(file, 'a') as f:
            f.write(line)
            f.write("\n")


gridSize_x = [10, 50, 100, 20, 100, 40, 80]
gridSize_y = [10, 50, 100, 100, 20, 80, 40]
robotsNumber_percent = [5, 10, 15, 20]
discs = [3, 10]

for i in range(0, len(gridSize_x)):
    for j in range(0, len(robotsNumber_percent)):
        for k in range(0, len(discs)):
            generator("results/free_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", gridSize_x[i], gridSize_y[i], robotsNumber_percent[j], discs[k])

# for i in range(0, len(gridSize_x)):
#     for j in range(0, len(robotsNumber_percent)):
#         for k in range(0, len(discs)):
#             generatorCells("results/grid_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt"", gridSize_x[i], gridSize_y[i], robotsNumber_percent[j], discs[k])

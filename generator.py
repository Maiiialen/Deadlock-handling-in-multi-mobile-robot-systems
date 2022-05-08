import random
import math

from numpy import correlate, greater
from Point import Point
from Grid import Grid
from Robot import Robot


def generator(file):
    lines = []
    robotPoints = []

    # grid
    grid_x_size = random.randint(20, 100)
    grid_y_size = random.randint(20, 100)
    cell_size = 2000
    line = "g " + str(grid_x_size) + " " + \
        str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    grid = Grid(grid_x_size, grid_y_size, cell_size, 1)

    # robots
    robots_number = random.randint(10, 100)
    for _ in range(0, robots_number):
        robot_size = math.floor((random.randint(5, 8)/10) * cell_size)
        robot_velocity = math.floor((random.randint(100, 500)))
        CorrectPlace = False
        while(not CorrectPlace):
            pos_x = random.randint(robot_size//2, grid_x_size*cell_size - robot_size//2)
            pos_y = random.randint(robot_size//2, grid_y_size*cell_size - robot_size//2)
            robot = Robot(1, 1, pos_x, pos_y, [])
            CorrectPlace = grid.addRobotPosition(robot, Point(pos_x, pos_y))
            # notCorrectPlace = False
            # for point in robotPoints:
            #     distance = int(math.hypot((point.x - pos_x),(point.y - pos_y)))
            #     if (distance) <= robot_size:
            #         notCorrectPlace = True
            #         break
        robotPoints.append(Point(pos_x, pos_y))
        line = "r " + str(robot_size) + " "+ str(robot_velocity) + " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = random.randint(3, 10)
        for _ in range(0, disc_number):
            disc_x = random.randint(robot_size//2, grid_x_size*cell_size - robot_size//2)
            disc_y = random.randint(robot_size//2, grid_y_size*cell_size - robot_size//2)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)

    with open(file, 'w') as f:
        f.write("")
    for line in lines:
        with open(file, 'a') as f:
            f.write(line)
            f.write("\n")


def generatorCells(file):
    lines = []
    robotPoints = []

    # grid
    grid_x_size = random.randint(20, 100)
    grid_y_size = random.randint(20, 100)
    cell_size = 2000
    line = "g " + str(grid_x_size) + " " + \
        str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    # robots
    robots_number = random.randint(10, 100)
    for _ in range(0, robots_number):
        robot_size = math.floor((random.randint(5, 8)/10) * cell_size)
        robot_velocity = math.floor((random.randint(100, 500)))
        notCorrectPlace = True
        while(notCorrectPlace):
            pos_x = random.randrange(cell_size//2, grid_x_size*cell_size - cell_size//2, cell_size)
            pos_y = random.randrange(cell_size//2, grid_y_size*cell_size - cell_size//2, cell_size)
            notCorrectPlace = False
            for point in robotPoints:
                if pos_x != point.x and pos_y != point.y:
                    notCorrectPlace = False
        line = "r " + str(robot_size) + " "+ str(robot_velocity) + " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = random.randint(3, 10)
        for _ in range(0, disc_number):
            disc_x = random.randrange(cell_size//2, grid_x_size*cell_size - cell_size//2, cell_size)
            disc_y = random.randrange(cell_size//2, grid_y_size*cell_size - cell_size//2, cell_size)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)

    with open(file, 'w') as f:
        f.write("")
    for line in lines:
        with open(file, 'a') as f:
            f.write(line)
            f.write("\n")

for i in range(0,1):
    generator("generated/generated_"+str(i)+".txt")

# for i in range(0,1000):
#     generatorCells("generatedCells/generatedCells_"+str(i)+".txt")
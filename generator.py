import random
import math

from numpy import correlate, greater
from Point import Point


def generator(file):
    lines = []
    robotPoints = []
    

    # grid
    grid_x_size = random.randint(10, 100)
    grid_y_size = random.randint(10, 100)
    cell_size = 2000
    line = "g " + str(grid_x_size) + " " + \
        str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    # robots
    robot_size = math.floor((random.randint(5, 9)/10) * cell_size)
    robots_number = random.randint(10, 100)
    for _ in range(0, robots_number):
        notCorrectPlace = True
        while(notCorrectPlace):
            pos_x = random.randint(robot_size//2, grid_x_size*cell_size - robot_size//2)
            pos_y = random.randint(robot_size//2, grid_y_size*cell_size - robot_size//2)
            notCorrectPlace = False
            for point in robotPoints:
                distance = int(math.hypot((point.x - pos_x),(point.y - pos_y)))
                if (distance) <= robot_size:
                    notCorrectPlace = True
                    print(str(distance) + ", " + str(robot_size))
                    break
        robotPoints.append(Point(pos_x, pos_y))
        line = "r " + str(robot_size) + " " + str(pos_x) + " " + str(pos_y)
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
    grid_x_size = random.randint(10, 100)
    grid_y_size = random.randint(10, 100)
    cell_size = 2000
    line = "g " + str(grid_x_size) + " " + \
        str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    # robots
    robot_size = math.floor((random.randint(5, 9)/10) * cell_size)
    robots_number = random.randint(10, 100)
    for _ in range(0, robots_number):
        notCorrectPlace = True
        while(notCorrectPlace):
            pos_x = random.randrange(cell_size//2, grid_x_size*cell_size - cell_size//2, cell_size)
            pos_y = random.randrange(cell_size//2, grid_y_size*cell_size - cell_size//2, cell_size)
            notCorrectPlace = False
            for point in robotPoints:
                if pos_x != point.x and pos_y != point.y:
                    notCorrectPlace = False
        line = "r " + str(robot_size) + " " + str(pos_x) + " " + str(pos_y)
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

generator("grid5.txt")
# generatorCells("grid6.txt")
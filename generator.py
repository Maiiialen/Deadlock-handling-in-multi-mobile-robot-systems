import random
import math
from Point import Point

def generator():
    lines = []

    # grid
    grid_x_size = random.randrange(10, 10000)
    grid_y_size = random.randrange(10, 10000)
    cell_size = random.randrange(200, 400)
    line = "g " + str(grid_x_size) + " " + str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    # robots
    robot_size = math.floor((random.randrange(5, 9)/10) * cell_size)
    robots_number = random.randrange(10, 100)
    for _ in range(0,robots_number):
        pos_x = random.randrange(0,grid_x_size)
        pos_y = random.randrange(0,grid_y_size)
        line = "r " + str(robot_size) + " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = random.randrange(3, 10)
        for _ in range(0,disc_number):
            disc_x = random.randrange(0,grid_x_size)
            disc_y = random.randrange(0,grid_y_size)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)
        
        end_x = random.randrange(0,grid_x_size)
        end_y = random.randrange(0,grid_y_size)
        line = "e " + str(end_x) + " " + str(end_y)
        lines.append(line)
    
    file = "grid2.txt"
    with open(file,'w') as f:
        f.write("")
    for line in lines:
        print(line)
        with open(file,'a') as f:
            f.write(line)
            f.write("\n")
    

def generatorCells():
    lines = []

    # grid
    grid_x_size = random.randrange(10, 10000)
    grid_y_size = random.randrange(10, 10000)
    cell_size = random.randrange(200, 400, 2)
    line = "g " + str(grid_x_size) + " " + str(grid_y_size) + " " + str(cell_size)
    lines.append(line)

    # robots
    robot_size = math.floor((random.randrange(5, 9)/10) * cell_size)
    robots_number = random.randrange(10, 100)
    for _ in range(0,robots_number):
        pos_x = random.randrange(cell_size/2,grid_x_size-cell_size/2, cell_size)
        pos_y = random.randrange(cell_size/2,grid_y_size-cell_size/2, cell_size)
        line = "r " + str(robot_size) + " " + str(pos_x) + " " + str(pos_y)
        lines.append(line)

        disc_number = random.randrange(3, 10)
        for _ in range(0,disc_number):
            disc_x = random.randrange(cell_size/2,grid_x_size-cell_size/2, cell_size)
            disc_y = random.randrange(cell_size/2,grid_y_size-cell_size/2, cell_size)
            line = "d " + str(disc_x) + " " + str(disc_y)
            lines.append(line)
    
    file = "grid3.txt"
    with open(file,'w') as f:
        f.write("")
    for line in lines:
        print(line)
        with open(file,'a') as f:
            f.write(line)
            f.write("\n")
    


    
generatorCells()


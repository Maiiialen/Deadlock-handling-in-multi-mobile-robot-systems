from types import CellType
import copy
from Robot import Robot
from Point import Point
from sympy import FallingFactorial


class Grid:
    x_cells: int
    y_cells: int
    cell_size: int
    cell_capacity: int
    grid: list

    def __init__(self, x_cells, y_cells, cell_size, cell_capacity):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.cell_size = cell_size
        self.cell_capacity = cell_capacity

        self.grid = []
        for _ in range(0, self.x_cells):
            row = []
            for _ in range(0, self.y_cells):
                row.append(0)
            self.grid.append(row)

    def printGrid(self):
        for i in range(0, self.x_cells):
            for j in range(0, self.y_cells):
                print(str(self.grid[i][j]), end=" ")
            print()
        print("Cell size: " + str(self.cell_size))

    def printTempGrid(self, grid):
        for i in range(0, self.x_cells):
            for j in range(0, self.y_cells):
                print(str(grid[i][j]), end=" ")
            print()

    def addRobotPosition(self, robot,  new_position):
        x = new_position.x//self.cell_size
        y = new_position.y//self.cell_size

        positions = []

        if not x < self.x_cells:
            x -= 1
        if not y < self.y_cells:
            y -= 1

        if self.grid[x][y] >= self.cell_capacity:
            return False
            
        # self.grid[x][y] += 1
        positions.append(Point(x, y))
        if new_position.x < x*self.cell_size + robot.size//2 and x > 0:
            if self.grid[x-1][y] >= self.cell_capacity:
                return False
            # self.grid[x-1][y] += 1
            positions.append(Point(x-1, y))
            if new_position.y < y*self.cell_size + robot.size//2 and y > 0:
                if self.grid[x][y-1] >= self.cell_capacity or self.grid[x-1][y-1] >= self.cell_capacity:
                    return False
                # self.grid[x][y-1] += 1
                # self.grid[x-1][y-1] += 1
                positions.append(Point(x, y-1))
                positions.append(Point(x-1, y-1))
            elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
                if self.grid[x][y+1] >= self.cell_capacity or self.grid[x-1][y+1] >= self.cell_capacity:
                    return False
                # self.grid[x][y+1] += 1
                # self.grid[x-1][y+1] += 1
                positions.append(Point(x, y+1))
                positions.append(Point(x-1, y+1))
        elif new_position.x > (x+1)*self.cell_size - robot.size//2 and x < self.x_cells-1:
            if self.grid[x+1][y] >= self.cell_capacity:
                return False
            # self.grid[x+1][y] += 1
            positions.append(Point(x+1, y))
            if new_position.y < y*self.cell_size + robot.size//2 and y > 0:
                if self.grid[x][y-1] >= self.cell_capacity or self.grid[x+1][y-1] >= self.cell_capacity:
                    return False
                # self.grid[x][y-1] += 1
                # self.grid[x+1][y-1] += 1
                positions.append(Point(x, y-1))
                positions.append(Point(x+1, y-1))
            elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
                if self.grid[x][y+1] >= self.cell_capacity or self.grid[x+1][y+1] >= self.cell_capacity:
                    return False
                # self.grid[x][y+1] += 1
                # self.grid[x+1][y+1] += 1
                positions.append(Point(x, y+1))
                positions.append(Point(x+1, y+1))
        elif new_position.y < y*self.cell_size + robot.size//2 and y > 0:
            if self.grid[x][y-1] >= self.cell_capacity:
                return False
            # self.grid[x][y-1] += 1
            positions.append(Point(x, y-1))
        elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
            if self.grid[x][y+1] >= self.cell_capacity:
                return False
            # self.grid[x][y+1] += 1
            positions.append(Point(x, y+1))
        for pos in positions:
            self.grid[pos.x][pos.y] += 1
        return True

    def removeRobotPosition(self, robot):
        x = robot.position_x//self.cell_size
        y = robot.position_y//self.cell_size
        if not x < self.x_cells:
            x -= 1
        if not y < self.y_cells:
            y -= 1
        self.grid[x][y] -= 1
        if robot.position_x < x*self.cell_size + robot.size//2 and x > 0:
            self.grid[x-1][y] -= 1
            if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                self.grid[x][y-1] -= 1
                self.grid[x-1][y-1] -= 1
            elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
                self.grid[x][y+1] -= 1
                self.grid[x-1][y+1] -= 1
        elif robot.position_x > (x+1)*self.cell_size - robot.size//2 and x < self.x_cells-1:
            self.grid[x+1][y] -= 1
            if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                self.grid[x][y-1] -= 1
                self.grid[x+1][y-1] -= 1
            elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
                self.grid[x][y+1] -= 1
                self.grid[x+1][y+1] -= 1
        elif robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
            self.grid[x][y-1] -= 1
        elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells-1:
            self.grid[x][y+1] -= 1

    # def updateRobotPosition(self, robot, new_position):
    #     temp_grid = copy.deepcopy(self.grid)

    #     self.removeRobotPosition(robot)
            
    #     if not self.addRobotPosition(robot, new_position):
    #         self.grid = copy.deepcopy(temp_grid)
    #         return False
    #     return True

    def updateRobotPosition(self, robot, new_position):
        old_position = Point(robot.position_x, robot.position_y)

        self.removeRobotPosition(robot)
            
        if not self.addRobotPosition(robot, new_position):
            self.addRobotPosition(robot, old_position)
            return False
        return True

from types import CellType
import copy
from Robot import Robot
from sympy import FallingFactorial


class Grid:
    x_cells: int
    y_cells: int
    cell_size: int
    grid: list

    def __init__(self, x_cells, y_cells, cell_size):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.cell_size = cell_size

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

    def addRobotPosition(self, robot):
        x = robot.position_x//self.cell_size
        y = robot.position_y//self.cell_size
        if self.grid[x][y] < 1:
            self.grid[x][y] += 1
            if robot.position_x < x*self.cell_size + robot.size//2 and x > 0:
                self.grid[x-1][y] += 1
                if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                    self.grid[x][y-1] += 1
                    self.grid[x-1][y-1] += 1
                elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                    self.grid[x][y+1] += 1
                    self.grid[x-1][y+1] += 1
            elif robot.position_x > (x+1)*self.cell_size - robot.size//2 and x < self.x_cells:
                self.grid[x+1][y] += 1
                if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                    self.grid[x][y-1] += 1
                    self.grid[x+1][y-1] += 1
                elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                    self.grid[x][y+1] += 1
                    self.grid[x+1][y+1] += 1
            elif robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                self.grid[x][y-1] += 1
            elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                self.grid[x][y+1] += 1
        # self.printGrid()

    def updateRobotPosition(self, robot, new_position):
        robot.printRobot()
        new_position.printp()
        temp_grid = copy.deepcopy(self.grid)
        x = robot.position_x//self.cell_size
        y = robot.position_y//self.cell_size
        temp_grid[x][y] -= 1
        if robot.position_x < x*self.cell_size + robot.size//2 and x > 0:
            temp_grid[x-1][y] -= 1
            if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                temp_grid[x][y-1] -= 1
                temp_grid[x-1][y-1] -= 1
            elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                temp_grid[x][y+1] -= 1
                temp_grid[x-1][y+1] -= 1
        elif robot.position_x > (x+1)*self.cell_size - robot.size//2 and x < self.x_cells:
            temp_grid[x+1][y] -= 1
            if robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
                temp_grid[x][y-1] -= 1
                temp_grid[x+1][y-1] -= 1
            elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                temp_grid[x][y+1] -= 1
                temp_grid[x+1][y+1] -= 1
        elif robot.position_y < y*self.cell_size + robot.size//2 and y > 0:
            temp_grid[x][y-1] -= 1
        elif robot.position_y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
            temp_grid[x][y+1] -= 1
        # print("MINUSES")
        # self.printTempGrid(temp_grid)
            
        x = new_position.x//self.cell_size
        y = new_position.y//self.cell_size

        if temp_grid[x][y] > 0:
            return False
        if temp_grid[x][y] < 1:
            temp_grid[x][y] += 1
            if new_position.x < x*self.cell_size + robot.size//2 and x > 0:
                temp_grid[x-1][y] += 1
                if new_position.y < y*self.cell_size + robot.size//2 and y > 0:
                    temp_grid[x][y-1] += 1
                    temp_grid[x-1][y-1] += 1
                elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                    temp_grid[x][y+1] += 1
                    temp_grid[x-1][y+1] += 1
            elif new_position.x > (x+1)*self.cell_size - robot.size//2 and x < self.x_cells:
                temp_grid[x+1][y] += 1
                if new_position.y < y*self.cell_size + robot.size//2 and y > 0:
                    temp_grid[x][y-1] += 1
                    temp_grid[x+1][y-1] += 1
                elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                    temp_grid[x][y+1] += 1
                    temp_grid[x+1][y+1] += 1
            elif new_position.y < y*self.cell_size + robot.size//2 and y > 0:
                temp_grid[x][y-1] += 1
            elif new_position.y > (y+1)*self.cell_size - robot.size//2 and y < self.y_cells:
                temp_grid[x][y+1] += 1
        self.grid = temp_grid
        # print("PLUSES")
        # self.printTempGrid(temp_grid)
        return True

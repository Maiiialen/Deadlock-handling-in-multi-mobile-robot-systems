from types import CellType


class Grid:
    x_cells: int
    y_cells: int
    cell_size: int

    def __init__(self, x_cells, y_cells, cell_size):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.cell_size = cell_size

        self.grid = []
        for _ in range(0, self.x_cells):
            row = []
            for _ in range(0, self.y_cells):
                row.append(5)
            self.grid.append(row)

    def printGrid(self):
        for i in range(0, self.x_cells):
            for j in range(0, self.y_cells):
                print(str(self.grid[i][j]), end=" ")
            print()
        print("Cell size: " + str(self.cell_size))

    def findLine(self, start, end):
        # https://iqcode.com/code/python/python-bresenham-line-algorithm
        
        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1
    
        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)
    
        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
    
        # Swap start and end points if necessary and store swap state
        swapped = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            swapped = True
    
        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1
    
        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1
    
        # Iterate over bounding box generating points between start and end
        y = y1
        points = []
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            points.append(coord)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx
    
        # Reverse the list if the coordinates were swapped
        if swapped:
            points.reverse()
        return points

    def pointsToCells(self, points, robot_x, robot_y):
        for point in points:
            i = int(point.x / self.cell_size)
            j = int(point.y / self.cell_size)
            if (self.grid[i][j] < 10):
                self.grid[i][j] += 1

            robot_i = int(robot_x / self.cell_size)
            robot_j = int(robot_y / self.cell_size)
            line_points = self.findLine((i, j), (robot_i, robot_j))

            for line_point in line_points:
                if (self.grid[line_point[0]][line_point[1]] > 0):
                    self.grid[line_point[0]][line_point[1]] -= 1
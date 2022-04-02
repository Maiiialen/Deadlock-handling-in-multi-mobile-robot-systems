from types import CellType


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
                row.append(5)
            self.grid.append(row)

    def printGrid(self):
        for i in range(0, self.x_cells):
            for j in range(0, self.y_cells):
                print(str(self.grid[i][j]), end=" ")
            print()
        print("Cell size: " + str(self.cell_size))

class Robot:
    size: int
    position_x: int
    position_y: int
    path: list

    def __init__(self, size, position_x, position_y, path):
        self.size = size
        self.position_x = position_x
        self.position_y = position_y
        self.path = path


    def printRobot(self):
        print("Robot:")
        print("\tsize: " + str(self.size))
        print("\tposition x: " + str(self.position_x) + " y: " + str(self.position_y))
        print("path:")
        for point in self.path:
            print("\t", end="")
            point.printp()


    
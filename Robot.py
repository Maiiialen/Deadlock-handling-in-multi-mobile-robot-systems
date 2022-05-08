from Point import Point
import math

class Robot:
    size: int
    velocity: int
    position_x: int
    position_y: int
    path: list
    blocked = 0
    goesBack = 0
    goesLeft = 0

    def __init__(self, size, velocity, position_x, position_y, path):
        self.size = size
        self.velocity = velocity
        self.position_x = position_x
        self.position_y = position_y
        self.path = []
        for point in path:
            self.path.append(point)

    def calculateMove(self, method):
        if method == 0:
            if len(self.path) > 0:
                distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
                if distance_to_end_point == 0:
                    self.goesBack = 0
                    self.path.pop(0)
            if len(self.path) > 0:
                distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
                if distance_to_end_point < self.velocity:
                    return self.path[0]
                else:
                    x_diff = self.position_x - self.path[0].x
                    if x_diff != 0:
                        alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff)))
                        if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                            new_x = int(self.position_x - math.cos(alpha)*self.velocity)
                            new_y = int(self.position_y - math.sin(alpha)*self.velocity)
                        elif self.path[0].y - self.position_y < 0:
                            new_x = int(self.position_x + math.cos(alpha)*self.velocity)
                            new_y = int(self.position_y - math.sin(alpha)*self.velocity)
                        elif self.path[0].x - self.position_x < 0:
                            new_x = int(self.position_x - math.cos(alpha)*self.velocity)
                            new_y = int(self.position_y + math.sin(alpha)*self.velocity)
                        else:
                            new_x = int(self.position_x + math.cos(alpha)*self.velocity)
                            new_y = int(self.position_y + math.sin(alpha)*self.velocity)
                        new_pos = Point(new_x, new_y)
                    else:
                        if self.path[0].y - self.position_y < 0:
                            new_pos = Point(int(self.position_x), int(self.position_y - self.velocity))
                        else:
                            new_pos = Point(int(self.position_x), int(self.position_y + self.velocity))
                    return new_pos
            return None
        else:
            if len(self.path) > 0:
                if self.position_x - self.path[0].x == 0 and self.position_y - self.path[0].y == 0:
                    self.path.pop(0)
                    self.goesBack = 0
            if len(self.path) > 0:
                x_diff = abs(self.position_x - self.path[0].x)
                y_diff = abs(self.position_y - self.path[0].y)
                if x_diff != 0:
                    if x_diff < self.velocity:
                        new_pos = Point(int(self.path[0].x), int(self.position_y))
                    elif self.path[0].x - self.position_x < 0:
                        new_pos = Point(int(self.position_x - self.velocity), int(self.position_y))
                    else:
                        new_pos = Point(int(self.position_x + self.velocity), int(self.position_y))
                else:
                    if y_diff < self.velocity:
                        new_pos = Point(int(self.position_x), int(self.path[0].y))
                    elif self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y - self.velocity))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y + self.velocity))
                return new_pos
        return None

    def move(self, new_point):
        self.position_x = new_point.x
        self.position_y = new_point.y

    def printRobot(self):
        print("Robot:")
        print("\tsize: " + str(self.size))
        print("\tposition x: " + str(self.position_x) + " y: " + str(self.position_y))
        print("path:")
        for point in self.path:
            print("\t", end="")
            point.printp()

    def goBack(self, method):
        if self.goesBack == 0:
            self.goesBack = 1
            if method == 0:
                x_diff = self.position_x - self.path[0].x
                if x_diff != 0:
                    alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff)))
                    if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x + math.cos(alpha)*self.size)
                        new_y = int(self.position_y + math.sin(alpha)*self.size)
                    elif self.path[0].y - self.position_y < 0:
                        new_x = int(self.position_x - math.cos(alpha)*self.size)
                        new_y = int(self.position_y + math.sin(alpha)*self.size)
                    elif self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x + math.cos(alpha)*self.size)
                        new_y = int(self.position_y - math.sin(alpha)*self.size)
                    else:
                        new_x = int(self.position_x - math.cos(alpha)*self.size)
                        new_y = int(self.position_y - math.sin(alpha)*self.size)
                    new_pos = Point(new_x, new_y)
                else:
                    if self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y + self.size))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y - self.size))
                self.path.insert(0, new_pos)
                return True
            else:
                if abs(self.position_x - self.path[0].x) != 0:
                    if self.path[0].x - self.position_x < 0:
                        new_pos = Point(int(self.position_x + self.size), int(self.position_y))
                    else:
                        new_pos = Point(int(self.position_x - self.size), int(self.position_y))
                else:
                    if self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y + self.size))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y - self.size))
                self.path.insert(0, new_pos)
                return True
        return False

    def goLeft(self, method, cellSize):
        self.goesBack = 1
        self.goesLeft = 1
        if method == 0:
            x_diff = self.position_x - self.path[0].x
            if x_diff != 0:
                alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff))) - math.pi/2
                if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                    new_x = int(self.position_x - math.cos(alpha)*cellSize)
                    new_y = int(self.position_y - math.sin(alpha)*cellSize)
                elif self.path[0].y - self.position_y < 0:
                    new_x = int(self.position_x + math.cos(alpha)*cellSize)
                    new_y = int(self.position_y - math.sin(alpha)*cellSize)
                elif self.path[0].x - self.position_x < 0:
                    new_x = int(self.position_x - math.cos(alpha)*cellSize)
                    new_y = int(self.position_y + math.sin(alpha)*cellSize)
                else:
                    new_x = int(self.position_x + math.cos(alpha)*cellSize)
                    new_y = int(self.position_y + math.sin(alpha)*cellSize)
                new_pos = Point(new_x, new_y)
            else:
                if self.path[0].y - self.position_y < 0:
                    new_pos = Point(int(self.position_x - cellSize), int(self.position_y))
                else:
                    new_pos = Point(int(self.position_x + cellSize), int(self.position_y))
            self.path.insert(0, new_pos)
            return True
        else:
            if abs(self.position_x - self.path[0].x) != 0:
                if self.path[0].x - self.position_x < 0:
                    new_pos = Point(int(self.position_x), int(self.position_y - cellSize))
                else:
                    new_pos = Point(int(self.position_x), int(self.position_y + cellSize))
            else:
                if self.path[0].y - self.position_y < 0:
                    new_pos = Point(int(self.position_x - cellSize), int(self.position_y))
                else:
                    new_pos = Point(int(self.position_x + cellSize), int(self.position_y))
            self.path.insert(0, new_pos)
            return True

    def goRight(self, method, cellSize):
        self.goesLeft = 0
        if method == 0:
            x_diff = self.position_x - self.path[0].x
            if x_diff != 0:
                alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff))) + math.pi/2
                if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                    new_x = int(self.position_x - math.cos(alpha)*cellSize)
                    new_y = int(self.position_y - math.sin(alpha)*cellSize)
                elif self.path[0].y - self.position_y < 0:
                    new_x = int(self.position_x + math.cos(alpha)*cellSize)
                    new_y = int(self.position_y - math.sin(alpha)*cellSize)
                elif self.path[0].x - self.position_x < 0:
                    new_x = int(self.position_x - math.cos(alpha)*cellSize)
                    new_y = int(self.position_y + math.sin(alpha)*cellSize)
                else:
                    new_x = int(self.position_x + math.cos(alpha)*cellSize)
                    new_y = int(self.position_y + math.sin(alpha)*cellSize)
                new_pos = Point(new_x, new_y)
            else:
                if self.path[0].y - self.position_y < 0:
                    new_pos = Point(int(self.position_x + cellSize), int(self.position_y))
                else:
                    new_pos = Point(int(self.position_x - cellSize), int(self.position_y))
            self.path.insert(0, new_pos)
            return True
        else:
            if abs(self.position_x - self.path[0].x) != 0:
                if self.path[0].x - self.position_x < 0:
                    new_pos = Point(int(self.position_x), int(self.position_y + cellSize))
                else:
                    new_pos = Point(int(self.position_x), int(self.position_y - cellSize))
            else:
                if self.path[0].y - self.position_y < 0:
                    new_pos = Point(int(self.position_x + cellSize), int(self.position_y))
                else:
                    new_pos = Point(int(self.position_x - cellSize), int(self.position_y))
            self.path.insert(0, new_pos)
            return True
    
    def changeSide(self, method, cellSize):
        if self.goesBack == 1:
            # print("path_1")
            # print(self.path[0].printp())
            # print(str(len(self.path)))
            self.path.pop(0)
            # print("path_2")
            # print(self.path[0].printp())
            if self.goesLeft == 0:
                self.goLeft(method, cellSize)
            elif self.goesLeft == 1:
                self.goRight(method, cellSize)
        return False

    def removePoint(self):
        self.path.pop(0)
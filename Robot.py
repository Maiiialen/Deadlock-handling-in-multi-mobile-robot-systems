from Point import Point
import math

class Robot:
    size: int
    velocity: int
    position_x: int
    position_y: int
    path: list
    blocked = 0
    isGoingBack = False
    isGoingBackInTwoSteps = False
    isGoingLeft = False
    pathSizeAfterPop:int
    sameSizeNumber = 0
    sameSizeNumberTwo = 0

    def __init__(self, size, velocity, position_x, position_y, path):
        self.size = size
        self.velocity = velocity
        self.position_x = position_x
        self.position_y = position_y
        self.path = []
        for point in path:
            self.path.append(point)
        self.pathSizeAfterPop = len(self.path)

    def calculateMoveEuclidian(self):
        if len(self.path) > 0:
            distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
            if distance_to_end_point == 0:
                self.path.pop(0)
                if self.isGoingBack:
                    self.isGoingBack = False
                    self.sameSizeNumber += 1
                else:
                    self.sameSizeNumber = 0
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

    def calculateMoveManhattan(self):
        if len(self.path) > 0:
            if self.position_x - self.path[0].x == 0 and self.position_y - self.path[0].y == 0:
                self.path.pop(0)
                if self.isGoingBackInTwoSteps:
                    self.isGoingBackInTwoSteps = False
                    self.sameSizeNumber += 1
                elif self.isGoingBack:
                    self.isGoingBack = False
                    self.sameSizeNumber += 1
                else:
                    self.sameSizeNumber = 0
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

    def calculateMove(self, method):
        if method == 0:
            new_pos = self.calculateMoveEuclidian()
        else:
            new_pos = self.calculateMoveManhattan()
        return new_pos

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

    def goBack(self, method, cellSize):
        if self.isGoingBack == 0:
            self.isGoingBack = 1
            if method == 0:
                x_diff = self.position_x - self.path[0].x
                if x_diff != 0:
                    alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff)))
                    if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x + math.cos(alpha)*cellSize)
                        new_y = int(self.position_y + math.sin(alpha)*cellSize)
                    elif self.path[0].y - self.position_y < 0:
                        new_x = int(self.position_x - math.cos(alpha)*cellSize)
                        new_y = int(self.position_y + math.sin(alpha)*cellSize)
                    elif self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x + math.cos(alpha)*cellSize)
                        new_y = int(self.position_y - math.sin(alpha)*cellSize)
                    else:
                        new_x = int(self.position_x - math.cos(alpha)*cellSize)
                        new_y = int(self.position_y - math.sin(alpha)*cellSize)
                    new_pos = Point(new_x, new_y)
                else:
                    if self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y + cellSize))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y - cellSize))
                self.path.insert(0, new_pos)
                return True
            else:
                if abs(self.position_x - self.path[0].x) != 0:
                    if self.path[0].x - self.position_x < 0:
                        new_pos = Point(int(self.position_x + cellSize), int(self.position_y))
                    else:
                        new_pos = Point(int(self.position_x - cellSize), int(self.position_y))
                else:
                    if self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y + cellSize))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y - cellSize))
                self.path.insert(0, new_pos)
                return True
        return False

    def goLeft(self, method, cellSize):
        self.isGoingLeft = 1
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
        self.isGoingLeft = 0
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
        if self.isGoingBack:
            self.removePoint()
        if not self.isGoingLeft:
            self.goLeft(method, cellSize)
        else:
            self.goRight(method, cellSize)

    

    def goToCenter(self, cellSize):
            self.isGoingBack = True
            self.isGoingBackInTwoSteps = True
            if abs(self.position_x - self.path[0].x) != 0:
                if self.path[0].x - self.position_x < 0:
                    if self.position_x%cellSize < 0.5*cellSize:
                        new_pos = Point(int(self.position_x//cellSize*cellSize + cellSize//2), int(self.position_y))
                    else:
                        new_pos = Point(int(((self.position_x//cellSize)+1)*cellSize + cellSize//2), int(self.position_y))
                else:
                    if self.position_x%cellSize < 0.5*cellSize:
                        new_pos = Point(int(self.position_x//cellSize*cellSize - cellSize//2), int(self.position_y))
                    else:
                        new_pos = Point(int(((self.position_x//cellSize))*cellSize + cellSize//2), int(self.position_y))
            else:
                if self.path[0].y - self.position_y < 0:
                    if self.position_y%cellSize < 0.5*cellSize:
                        new_pos = Point(int(self.position_x), int(self.position_y//cellSize*cellSize + cellSize//2))
                    else:
                        new_pos = Point(int(self.position_x), int(((self.position_y//cellSize)+1)*cellSize + cellSize//2))
                else:
                    if self.position_y%cellSize < 0.5*cellSize:
                        new_pos = Point(int(self.position_x), int(self.position_y//cellSize*cellSize - cellSize//2))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y//cellSize*cellSize + cellSize//2))
            self.path.insert(0, new_pos)

    def goLeftFromPath(self, cellSize):
        self.isGoingLeft = 1
        if abs(self.position_x - self.path[0].x) != 0:
            if self.path[0].x - self.position_x < 0:
                new_pos = Point(int(self.path[0].x), int(self.path[0].y - cellSize))
            else:
                new_pos = Point(int(self.path[0].x), int(self.path[0].y + cellSize))
        else:
            if self.path[0].y - self.position_y < 0:
                new_pos = Point(int(self.path[0].x - cellSize), int(self.path[0].y))
            else:
                new_pos = Point(int(self.path[0].x + cellSize), int(self.path[0].y))
        self.path.insert(1, new_pos)
        return True

    def goRightFromPath(self, cellSize):
        self.isGoingLeft = 0
        if abs(self.position_x - self.path[0].x) != 0:
            if self.path[0].x - self.position_x < 0:
                new_pos = Point(int(self.path[0].x), int(self.path[0].y + cellSize))
            else:
                new_pos = Point(int(self.path[0].x), int(self.path[0].y - cellSize))
        else:
            if self.path[0].y - self.position_y < 0:
                new_pos = Point(int(self.path[0].x + cellSize), int(self.path[0].y))
            else:
                new_pos = Point(int(self.path[0].x - cellSize), int(self.path[0].y))
        self.path.insert(1, new_pos)
        return True
    
    def changeSideGrid(self, cellSize):
        if self.isGoingBack:
            self.removePoint()
            if self.isGoingBackInTwoSteps:
                self.removePoint()
                self.isGoingBackInTwoSteps = False
            self.isGoingBack = False
        if int(self.position_x%cellSize) - cellSize//2 != 0 or int(self.position_y%cellSize) - cellSize//2 != 0:
            self.goToCenter(cellSize)
            self.isGoingBackInTwoSteps = True
        if not self.isGoingLeft:
            self.goLeftFromPath(cellSize)
        else:
            self.goRightFromPath(cellSize)
        self.isGoingBack = True

    def removePoint(self):
        self.path.pop(0)

    def removePointTwo(self):
        self.path.pop(1)
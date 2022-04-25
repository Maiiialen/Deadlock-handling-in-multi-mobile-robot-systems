from Point import Point
import math

class Robot:
    size: int
    velocity: int
    position_x: int
    position_y: int
    blocked: int
    path: list

    def __init__(self, size, velocity, position_x, position_y, path):
        self.size = size
        self.velocity = velocity
        self.position_x = position_x
        self.position_y = position_y
        self.blocked = 0
        self.path = []
        for point in path:
            self.path.append(point)

    def calculateMove(self, method):
        if method == 0:
            if len(self.path) > 0:
                distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
                if distance_to_end_point == 0:
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
                distance_to_end_point = int(abs((self.position_x - self.path[0].x) + (self.position_y - self.path[0].y)))
                if distance_to_end_point == 0 and (self.position_x - self.path[0].x == 0 or self.position_y - self.path[0].y == 0):
                    self.path.pop(0)
            if len(self.path) > 0:
                distance_to_end_point = int(abs((self.position_x - self.path[0].x) + (self.position_y - self.path[0].y)))
                if distance_to_end_point < self.velocity and (self.position_x - self.path[0].x == 0 or self.position_y - self.path[0].y == 0):
                    return self.path[0]
                else:
                    x_diff = self.position_x - self.path[0].x
                    if x_diff != 0:
                        if self.path[0].x - self.position_x < 0:
                            new_pos = Point(int(self.position_x - self.velocity), int(self.position_y))
                        else:
                            new_pos = Point(int(self.position_x + self.velocity), int(self.position_y))
                    else:
                        if self.path[0].y - self.position_y < 0:
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


    
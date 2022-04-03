from Point import Point
import math

ROBOT_SPEED = 1000     # mm/s(clock's pic)

class Robot:
    size: int
    position_x: int
    position_y: int
    blocked: int
    path: list

    def __init__(self, size, position_x, position_y, path):
        self.size = size
        self.position_x = position_x
        self.position_y = position_y
        self.blocked = 0
        self.path = []
        for point in path:
            self.path.append(point)

    def calculateMove(self):
        # self.path[0].printp()
        # print("x: " + str(self.position_x) + ", y: " + str(self.position_y))
        if len(self.path) > 0:
            distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
            if distance_to_end_point == 0:
                self.path.pop(0)
        if len(self.path) > 0:
            distance_to_end_point = int(math.hypot((self.position_x - self.path[0].x), (self.position_y - self.path[0].y)))
            if distance_to_end_point < ROBOT_SPEED:
                return self.path[0]
            else:
                x_diff = self.position_x - self.path[0].x
                if x_diff != 0:
                    alpha = math.atan(abs((self.position_y - self.path[0].y)/(x_diff)))
                    if self.path[0].y - self.position_y < 0 and self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x - math.cos(alpha)*ROBOT_SPEED)
                        new_y = int(self.position_y - math.sin(alpha)*ROBOT_SPEED)
                    elif self.path[0].y - self.position_y < 0:
                        new_x = int(self.position_x + math.cos(alpha)*ROBOT_SPEED)
                        new_y = int(self.position_y - math.sin(alpha)*ROBOT_SPEED)
                    elif self.path[0].x - self.position_x < 0:
                        new_x = int(self.position_x - math.cos(alpha)*ROBOT_SPEED)
                        new_y = int(self.position_y + math.sin(alpha)*ROBOT_SPEED)
                    else:
                        new_x = int(self.position_x + math.cos(alpha)*ROBOT_SPEED)
                        new_y = int(self.position_y + math.sin(alpha)*ROBOT_SPEED)
                    new_pos = Point(new_x, new_y)
                else:
                    if self.path[0].y - self.position_y < 0:
                        new_pos = Point(int(self.position_x), int(self.position_y - ROBOT_SPEED))
                    else:
                        new_pos = Point(int(self.position_x), int(self.position_y + ROBOT_SPEED))
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


    
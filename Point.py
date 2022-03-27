class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printp(self):
        print("x: " + str(self.x) + " y: " + str(self.y))
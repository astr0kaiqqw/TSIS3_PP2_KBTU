import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance
point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()  
point2.show()  

point1.move(4, 4)
point1.show()  

distance = point1.dist(point2)
print(f"Distance between points: {distance}") 

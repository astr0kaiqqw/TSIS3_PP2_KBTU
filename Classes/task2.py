class Shape:
    def __init__(self):
        self.area_value = 0  

    def area(self):
        print(f"The area of the shape is: {self.area_value}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length

    def area(self):
        self.area_value = self.length ** 2
        print(f"The area of the square is: {self.area_value}")



shape = Shape()
shape.area() 

square = Square(5)
square.area()  

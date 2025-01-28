class Shape:
    def __init__(self):
        self.area_value = 0  # Площадь по умолчанию равна 0

    def area(self):
        print(f"The area of the shape is: {self.area_value}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width

    def area(self):
        self.area_value = self.length * self.width
        print(f"The area of the rectangle is: {self.area_value}")



shape = Shape()
shape.area() 

rectangle = Rectangle(4, 5)
rectangle.area()  

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y

class Circle(Shape):


    def area(self):
        return 3.14*super().area()
sq = Shape(3,5)
print(sq.area())


c = Circle(5)
print(c.area())
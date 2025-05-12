import math
class Shape:
    def area(self):
        pass
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius)**2
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth

s=Shape()  
c=Circle(5)
r=Rectangle(10,5)
shapes = [c, r]

# Loop through and call area() on each
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
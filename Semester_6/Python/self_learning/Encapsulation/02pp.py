# Create a class Circle with:

# Private attribute __radius

# Method to get and set radius 
# (with validation: must be positive)

# Method to calculate and return area
import math
class Circle:
    def __init__(self,radius):
        self.__radius=radius
    def get_raduis(self):
        return self.__radius
    def set_raduis(self,radius):
        if radius> 0:
            self.__radius=radius
        else:
            print("invalid radius")

    def area(self):
        return math.pi*(self.__radius**2)
c = Circle(5)
print("Radius:", c.get_radius())     # 5
print("Area:", c.area())             # Should print area of circle

c.set_radius(10)
print("Updated Radius:", c.get_radius())   # 10
print("Updated Area:", c.area())           # Updated area

#c.set_radius(-2)  # ❌ Invalid radius

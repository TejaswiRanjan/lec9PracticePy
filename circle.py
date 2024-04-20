#Define a Circle to create a circle with radius r using the constructor. Define an Area() method of the class which calculate the area of the circle. Define a perimeter() method of the class which allows you to calculate the perimeter of Circle.

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (3.14*self.radius**2)
    
    def perimeter(self):
        return (2*3.14*self.radius)
    
c1 = Circle(3)
print("Area of Circle is : ",c1.area())
print("Perimeter of circle is : ",c1.perimeter()) 
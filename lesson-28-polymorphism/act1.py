
"""
************
The Question
************

Consider a Python program designed around geometric shapes using Object-Oriented
Programming (OOP). The program features a central, abstract template called Shape
that forces any specific geometric figure to include a method for finding its size
called calculate_area(). Three distinct classes—Circle, Square, and Triangle—adopt
this template, each writing its own specific math formula to compute its unique area.
Your task is to write a Python script that showcases this setup. First, define the 
abstract Shape base class along with its three specific child classes. 
Then, create a single Python list containing one instance of each shape 
(a circle, a square, and a triangle) with dimensions of your choice. 
Finally, write a loop that iterates through this mixed list, 
automatically triggers the correct area formula for each object without manually 
checking its specific class type, and prints each calculated area formatted to 
two decimal places.

"""

# Answer code

import math
from abc import ABC, abstractmethod
from typing import override

# parent Abstract class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# implement circle
class circle(Shape):
    def __init__(self,radius):
        self.radius = radius    
    @override
    def calculate_area(self):
        return math.pi*(self.radius**2)

# implement square
class Square(Shape):
    def __init__(self,side):
        self.side = side
    @override
    def calculate_area(self):
       return (self.side**2)

# implement triangle
class Triangle(Shape):  
    def __init__(self,base,height):
        self.base = base
        self.height = height
    @override
    def calculate_area(self):
       return 0.5*(self.height*self.base)  
    
Shapes_list = [circle(5) , Square(7), Triangle(5,7)]

for shape in Shapes_list:
    area = shape.calculate_area()
    print(f"The area of{shape.__class__.__name__}:{area:.2f}")
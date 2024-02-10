from math import *
class Circle(object):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        print(pi*self.r**2)
    def getPerimeter(self):
        print(2*pi*self.r)

circle = Circle(4.44)
circle.getPerimeter()
circle2 = Circle(11)
circle2.getArea()
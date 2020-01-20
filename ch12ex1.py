# Exercise 12.1
# Design a class named Triangle that extends the GeometricObject class
# Sawan Srivastava
# 1/19/2020
from GeometricObject import GeometricObject
import math
class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def getSide1(self):
        return self.__side1
    def getSide2(self):
        return self.__side2
    def getSide3(self):
        return self.__side3
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return format(math.sqrt((s*(s-self.__side1))*(s-self.__side2)*(s-self.__side3)), ".2f")
    def getPerimeter(self):
        return format(side1+side2+side3, ".2f")
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str (self.__side2) + " side3 = " + str(self.__side3)
t1 = Triangle(5, 10)
print(t1)

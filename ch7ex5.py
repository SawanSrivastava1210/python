# Exercise 7.5
# Create a class Regular Polygon which calculates the area and perimeter  of the polygon
# Sawan Srivastava
# 1/15/2020
import math
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def set_n (self, n):
        self.__n = n

    def set_side (self, side):
        self.__side = side

    def set_x (self, x):
        self.__x = x

    def set_y (self, y):
        self.__y = y

    def get_n (self):
        return self.__n

    def get_side (self):
        return self.__side

    def get_x (self):
        return self.__x

    def get_y (self):
        return self.__y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        return (self.__n * self.__side**2)/4*math.tan(math.pi/self.__n)
Shape1 = RegularPolygon()
Shape2 = RegularPolygon(6, 4)
Shape3 = RegularPolygon(10, 4, 5.6, 7.8)
print('The perimeter of Shape1 is',Shape1.getPerimeter())
print('The area of Shape1 is',Shape1.getArea())
print('The perimeter of Shape2 is',Shape2.getPerimeter())
print('The area of Shape2 is',Shape2.getArea())
print('The perimeter of Shape3 is',Shape3.getPerimeter())
print('The area of Shape3 is',Shape3.getArea())


        
        
        
            

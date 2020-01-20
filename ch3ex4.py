# Exercise 3.4
# prompts the user to enter the side of a pentagon and displays the area
# Sawan Srivastava
# 1/6/2020
import math
Side = eval(input('Enter the side:'))
Area = (5*Side**2)/(4*math.tan(math.pi/5))
print('The area of the pentagon with side',Side,'is',Area)

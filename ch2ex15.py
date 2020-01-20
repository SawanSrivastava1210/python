# Exercise 2.15
# prompts the user to enter the side of a hexagon and displays its area
# Sawan Srivastava
# 1/3/2020

#Asks user for input
Side = eval(input('Enter the side: '))

#Calculates area of hexagon
Area = ((3*3**0.5)/2)*Side**2

#Prints out the area of the hexagon
print('The area of the hexagon with side',Side,'is', Area)

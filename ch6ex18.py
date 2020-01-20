# Exercise 6.18
# Contains one function printMatrix which prints a matrix with the dimensions given  
# Sawan Srivastava
# 1/13/2020
import random
n = eval(input('Enter n: '))
def printMatrix(n):
    for k in range(n):
        for l in range(n):
            print(str(random.randint(0, 1))+' ', end='')
        print('')
def main():
    printMatrix(n)

main()

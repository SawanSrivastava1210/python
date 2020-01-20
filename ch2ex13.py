# Exercise 2.13
# prompts the user to enter a four-digit integer and displays the number in reverse order
# Sawan Srivastava
# 1/3/2020

#Asks user for input
Integer = eval(input('Enter a four digit integer: '))
if (Integer//10000>0):
    Integer = eval(input('Please enter a four digit integer: '))

#Finding digits
Dig1 = Integer//1000
Dig2 = (Integer-(Dig1*1000))//100
Dig3 = (Integer-(Dig1*1000)-(Dig2*100))//10
Dig4 = Integer%10

#Printing out the digits
print(Dig1)
print(Dig2)
print(Dig3)
print(Dig4)

MILE = 23
print (MILE)

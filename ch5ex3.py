# Exercise 5.3
# prints out conversion table for kilograms to pounds until kilograms exceed 200
# Sawan Srivastava
# 1/10/2020
Kilograms = 1
print('Kilograms     Pounds')
while Kilograms < 200:
    Pounds = Kilograms*2.2
    print (Kilograms,'           ',format(Pounds,".1f"))
    Kilograms += 2

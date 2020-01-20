# Exercise 2.5
# Reads the subtotal and the gratuity rate and computes the gratuity and total
# Sawan Srivastava
# 1/3/2020

#Ask the user for input
Subtotal, GratuityRate = eval(input("Enter the subtotal and a gratuity rate seperated with a comma: " ))

#Calculate Total and Gratuity
Gratuity = Subtotal*(GratuityRate/100)
Total = Subtotal + Gratuity

#Print out Total and Gratuity
print("The gratuity is", Gratuity ,"and the total is", Total)

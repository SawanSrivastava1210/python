# Exercise 4.7
# reads amount of money and prints out the amount in dollars, quarters, dimes, nickels, and pennies
# Sawan Srivastava
# 1/7/2020

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))
#enter input
# Convert the amount to cents
remainingAmount = int(amount * 100)
# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100 
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25 
# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10 
# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5 
# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount
print('Your amount', amount, 'consists of')
if numberOfOneDollars != 0:
    if numberOfOneDollars == 1:
        print(numberOfOneDollars, 'dollar')
    else:
        print(numberOfOneDollars, 'dollars')
if numberOfQuarters != 0:
    if numberOfQuarters == 1:
        print(numberOfQuarters, 'quarter')
    else:
        print(numberOfQuarters, 'quarters')
if numberOfDimes != 0:
    if numberOfDimes == 1:
        print(numberOfDimes, 'dime')
    else:
        print(numberOfDimes, 'dimes')
if numberOfNickels != 0:
    if numberOfNickels == 1:
        print(numberOfNickels, 'nickel')
    else:
        print(numberOfNickels, 'nickels')
if numberOfPennies != 0:
    if numberOfPennies == 1:
        print(numberOfPennies, 'penny')
    else:
        print(numberOfPennies, 'pennies')

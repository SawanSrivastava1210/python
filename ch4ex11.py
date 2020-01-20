# Exercise 4.11
# prompts the user to enter the month and year and displays the number of days in the month
# Sawan Srivastava
# 1/7/2020
Month = input('Please enter the month: ')
Year = eval(input('Please enter the year: '))
if Month    == 'January':
    print(Month, Year,'has 31 days')
elif Month == 'February':
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        print(Month, Year,'has 29 days')       
    else:
        print(Month, Year,'has 28 days')
elif Month == 'March':
    print(Month, Year,'has 31 days')
elif Month == 'April':
    print(Month, Year,'has 30 days')
elif Month == 'May':
    print(Month, Year,'has 31 days')
elif Month == 'June':
    print(Month, Year,'has 30 days')
elif Month == 'July':
    print(Month, Year,'has 31 days')
elif Month == 'August':
    print(Month, Year,'has 31 days')
elif Month == 'September':
    print(Month, Year,'has 30 days')
elif Month == 'October':
    print(Month, Year,'has 31 days')
elif Month == 'November':
    print(Month, Year,'has 30 days')
elif Month == 'December':
    print(Month, Year,'has 31 days')


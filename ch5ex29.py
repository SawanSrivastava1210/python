# Exercise 5.29
# displays the characters in the ASCII character table from ! to ~
# Sawan Srivastava
# 1/10/2020
Year = 2001
i = 0
while 2001 <= Year <= 2100:
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        print(str(Year)+' ', end = '')
    Year += 1
    i += 1
    if i % 40 == 0:
        print()
        i = 0

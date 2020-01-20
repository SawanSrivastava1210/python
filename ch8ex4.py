# Exercise 8.4
# finds the number of occurrences of a specified character in a string
# Sawan Srivastava
# 1/15/2020
def count(s, ch):
    counter = 0
    for c in s:
        if c == ch:
            counter += 1    
    print(ch,'is in',s,counter, 'times')
count('Welcome', 'e')
        

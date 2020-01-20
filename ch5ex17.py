# Exercise 5.17
# displays the characters in the ASCII character table from ! to ~
# Sawan Srivastava
# 1/10/2020
Ascii = 33
i = 0
while 33 <= Ascii <= 126:
    print(chr(Ascii)+' ', end = '')
    Ascii += 1
    i = i + 1
    if i % 10 == 0:
        print()
        i = 0
        

    
          

   
    
    

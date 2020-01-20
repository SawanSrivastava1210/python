# Exercise 4.17
# plays rock paper scissors with the computer
# Sawan Srivastava
# 1/8/2020
import random
UserInput = eval(input('scissor (0), rock (1), paper (2): '))
ComputerInput = random.randint(0,2)
if UserInput == 0:
    UserChoice = 'scissor'
elif UserInput == 1:
    UserChoice = 'rock'
elif UserInput == 2:
    UserChoice = 'paper'
ComputerChoice = 'scissor' if ComputerInput == 0 elif ComputerInput == 1 'rock' elif ComputerInput == 2 'paper'    
if ComputerInput == 0:
    ComputerChoice = 'scissor'
elif ComputerInput == 1:
    ComputerChoice = 'rock'
elif ComputerInput == 2:
    ComputerChoice = 'paper'

if UserChoice == 'scissor' and ComputerChoice == 'paper':
    print('The computer is %s. You are %s. You Win!' % (ComputerChoice, UserChoice))
elif UserChoice == 'scissor' and ComputerChoice == 'rock':
    print('The computer is %s. You are %s. You Lose.' % (ComputerChoice, UserChoice))
elif UserChoice == 'scissor' and ComputerChoice == 'scissor':
    print('The computer is %s. You are %s too. It is a draw.' % (ComputerChoice, UserChoice))

if UserChoice == 'rock' and ComputerChoice == 'paper':
    print('The computer is %s. You are %s. You Lose.' % (ComputerChoice, UserChoice))
elif UserChoice == 'rock' and ComputerChoice == 'rock':
    print('The computer is %s. You are %s too. It is a draw.' % (ComputerChoice, UserChoice))
elif UserChoice == 'rock' and ComputerChoice == 'scissor':
    print('The computer is %s. You are %s. You Win!' % (ComputerChoice, UserChoice))

if UserChoice == 'paper' and ComputerChoice == 'paper':
    print('The computer is %s. You are %s too. It is a draw' % (ComputerChoice, UserChoice))
elif UserChoice == 'paper' and ComputerChoice == 'rock':
    print('The computer is %s. You are %s. You Win!' % (ComputerChoice, UserChoice))
elif UserChoice == 'paper' and ComputerChoice == 'scissor':
    print('The computer is %s. You are %s. You lose.' % (ComputerChoice, UserChoice))

#>>> 
#============= RESTART: /home/sawan/Python IDLE CIS007/ch4ex17.py =============
#scissor (0), rock (1), paper (2): 0
#The computer is paper. You are scissor. You Win!
#>>>     
    

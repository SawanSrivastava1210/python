# Exercise 3.13
# Write a program that displays a stop sign
# Sawan Srivastava
# 1/6/2020
import turtle
turtle.hideturtle()
turtle.left(150)
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() 
turtle.color("red")
turtle.circle(100, steps = 6)
turtle.end_fill()
turtle.color("white")
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.left(120)
turtle.forward(30)
turtle.pendown()
turtle.write('STOP', font=( " Arial " ,50, " normal " ))
turtle.done()



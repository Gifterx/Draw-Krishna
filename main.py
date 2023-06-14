import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(2)
t.pensize(3)

# Draw Radha
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("red")
t.circle(50)
t.penup()
t.goto(-125, -50)
t.pendown()
t.circle(25)
t.penup()
t.goto(-75, -50)
t.pendown()
t.circle(25)

# Draw Krishna
t.penup()
t.goto(100, -100)
t.pendown()
t.color("blue")
t.circle(50)
t.penup()
t.goto(75, -50)
t.pendown()
t.right(60)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

# Hide the turtle
t.hideturtle()

# Exit on click
screen.exitonclick()

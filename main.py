import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
krishna = turtle.Turtle()
krishna.speed(3)  # Set the drawing speed (1-10, where 1 is the slowest)

# Draw Krishna's face
krishna.penup()
krishna.goto(0, -150)  # Position the turtle to start drawing the face
krishna.pendown()
krishna.fillcolor("tan")
krishna.begin_fill()
krishna.circle(150)  # Draw a circle for the face
krishna.end_fill()

# Draw Krishna's peacock feather
krishna.penup()
krishna.goto(50, 80)  # Position the turtle to start drawing the peacock feather
krishna.pendown()
krishna.fillcolor("green")
krishna.begin_fill()
krishna.right(140)
krishna.forward(100)
krishna.right(120)
krishna.forward(100)
krishna.right(120)
krishna.forward(100)
krishna.right(140)
krishna.forward(100)
krishna.right(140)
krishna.forward(100)
krishna.right(120)
krishna.forward(100)
krishna.right(120)
krishna.forward(100)
krishna.end_fill()

# Draw Krishna's eyes
krishna.penup()
krishna.goto(-40, 20)  # Position the turtle to draw the left eye
krishna.pendown()
krishna.fillcolor("black")
krishna.begin_fill()
krishna.circle(30)  # Draw the left eye
krishna.end_fill()

krishna.penup()
krishna.goto(40, 20)  # Position the turtle to draw the right eye
krishna.pendown()
krishna.fillcolor("black")
krishna.begin_fill()
krishna.circle(30)  # Draw the right eye
krishna.end_fill()

# Draw Krishna's smile
krishna.penup()
krishna.goto(-60, -20)  # Position the turtle to draw the smile
krishna.pendown()
krishna.right(90)
krishna.circle(60, 180)  # Draw a semicircle for the smile

# Draw Krishna's crown
krishna.penup()
krishna.goto(-70, 180)  # Position the turtle to draw the crown
krishna.pendown()
krishna.fillcolor("yellow")
krishna.begin_fill()
krishna.forward(140)
krishna.right(120)
krishna.forward(140)
krishna.right(120)
krishna.forward(140)
krishna.end_fill()

# Hide the turtle and display the drawing
krishna.hideturtle()

turtle.done()

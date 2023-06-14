import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
krishna = turtle.Turtle()
krishna.speed(3)  # Set the drawing speed (1-10, where 1 is the slowest)

# Draw Lord Krishna's face
krishna.penup()
krishna.goto(0, -100)  # Position the turtle to start drawing the face
krishna.pendown()
krishna.circle(100)  # Draw a circle for the face

# Draw Krishna's eyes
krishna.penup()
krishna.goto(-40, 0)  # Position the turtle to draw the left eye
krishna.pendown()
krishna.fillcolor("black")
krishna.begin_fill()
krishna.circle(15)  # Draw the left eye
krishna.end_fill()

krishna.penup()
krishna.goto(40, 0)  # Position the turtle to draw the right eye
krishna.pendown()
krishna.fillcolor("black")
krishna.begin_fill()
krishna.circle(15)  # Draw the right eye
krishna.end_fill()

# Draw Krishna's smile
krishna.penup()
krishna.goto(-40, -30)  # Position the turtle to draw the smile
krishna.pendown()
krishna.circle(40, 180)  # Draw a semicircle for the smile

# Draw Krishna's flute
krishna.penup()
krishna.goto(-75, 100)  # Position the turtle to draw the flute
krishna.pendown()
krishna.fillcolor("brown")
krishna.begin_fill()
krishna.forward(150)
krishna.left(90)
krishna.forward(20)
krishna.left(90)
krishna.forward(20)
krishna.right(90)
krishna.forward(10)
krishna.right(90)
krishna.forward(20)
krishna.left(90)
krishna.forward(20)
krishna.left(90)
krishna.forward(150)
krishna.left(90)
krishna.forward(40)
krishna.left(90)
krishna.forward(20)
krishna.right(90)
krishna.forward(10)
krishna.right(90)
krishna.forward(20)
krishna.left(90)
krishna.forward(20)
krishna.left(90)
krishna.forward(40)
krishna.end_fill()

# Hide the turtle and display the drawing
krishna.hideturtle()

turtle.done()

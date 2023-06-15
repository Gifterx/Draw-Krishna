import turtle

# Load the image
image_path = "images.png"

# Register the image as a turtle shape
turtle.register_shape(image_path)

# Create a turtle object
image_turtle = turtle.Turtle()

# Set the turtle shape to the registered image
image_turtle.shape(image_path)

# Stretch the image
stretch_factor_x = 2  # Adjust as desired
stretch_factor_y = 1  # Adjust as desired
image_turtle.shapesize(stretch_factor_x, stretch_factor_y)

# Move the turtle to the desired position
image_turtle.goto(-100, 100)  # Adjust the coordinates as desired

# Hide the turtle and keep the image displayed
image_turtle.hideturtle()

turtle.done()


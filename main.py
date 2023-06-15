import turtle

screen = turtle.Screen()
screen.setup(500, 500)
hanuman = turtle.Turtle()
hanuman.speed(2)

# Draw face
hanuman.penup()
hanuman.goto(0, -100)
hanuman.pendown()
hanuman.begin_fill()
hanuman.color("orange")
hanuman.circle(100)
hanuman.end_fill()

# Draw eyes
hanuman.penup()
hanuman.goto(-40, 0)
hanuman.pendown()
hanuman.begin_fill()
hanuman.color("white")
hanuman.circle(20)
hanuman.end_fill()

hanuman.penup()
hanuman.goto(40, 0)
hanuman.pendown()
hanuman.begin_fill()
hanuman.color("white")
hanuman.circle(20)
hanuman.end_fill()

# Draw mouth
hanuman.penup()
hanuman.goto(-40, -40)
hanuman.pendown()
hanuman.width(3)
hanuman.color("black")
hanuman.right(90)
hanuman.circle(40, 180)

# Draw crown
hanuman.penup()
hanuman.goto(0, 50)
hanuman.pendown()
hanuman.width(5)
hanuman.color("red")
hanuman.goto(-40, 80)
hanuman.goto(-80, 120)
hanuman.goto(-20, 100)
hanuman.goto(40, 80)
hanuman.goto(80, 120)
hanuman.goto(20, 100)
hanuman.goto(0, 50)

# Draw body
hanuman.penup()
hanuman.goto(-60, -180)
hanuman.pendown()
hanuman.begin_fill()
hanuman.color("lightblue")
hanuman.circle(80)
hanuman.end_fill()

# Draw arms
hanuman.penup()
hanuman.goto(-100, -100)
hanuman.pendown()
hanuman.width(10)
hanuman.color("brown")
hanuman.goto(-160, -80)

hanuman.penup()
hanuman.goto(100, -100)
hanuman.pendown()
hanuman.width(10)
hanuman.color("brown")
hanuman.goto(160, -80)

# Draw tail
hanuman.penup()
hanuman.goto(-70, -260)
hanuman.pendown()
hanuman.width(8)
hanuman.color("brown")
hanuman.goto(-80, -320)
hanuman.goto(-40, -350)
hanuman.goto(0, -330)

hanuman.penup()
hanuman.goto(70, -260)
hanuman.pendown()
hanuman.width(8)
hanuman.color("brown")
hanuman.goto(80, -320)
hanuman.goto(40, -350)
hanuman.goto(0, -330)

hanuman.hideturtle()
screen.exitonclick()

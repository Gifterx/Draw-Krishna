import turtle

screen = turtle.Screen()
screen.setup(500, 500)
doge = turtle.Turtle()
doge.speed(2)

doge.begin_fill()
doge.color("lightgray")
doge.circle(100)
doge.end_fill()

doge.penup()
doge.goto(-30, 50)
doge.pendown()
doge.begin_fill()
doge.color("white")
doge.circle(20)
doge.end_fill()

doge.penup()
doge.goto(30, 50)
doge.pendown()
doge.begin_fill()
doge.color("white")
doge.circle(20)
doge.end_fill()

doge.penup()
doge.goto(0, 20)
doge.pendown()
doge.begin_fill()
doge.color("black")
doge.circle(10)
doge.end_fill()

doge.penup()
doge.goto(-30, -30)
doge.pendown()
doge.circle(50, 180)

doge.penup()
doge.goto(-100, 120)
doge.pendown()
doge.begin_fill()
doge.color("lightgray")
doge.circle(30)
doge.end_fill()

doge.penup()
doge.goto(100, 120)
doge.pendown()
doge.begin_fill()
doge.color("lightgray")
doge.circle(30)
doge.end_fill()

doge.hideturtle()
screen.exitonclick()


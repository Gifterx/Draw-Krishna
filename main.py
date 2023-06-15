from svgpathtools import svg2paths2, Path, Line
from tkinter import Tk, filedialog
import turtle

root = Tk()
root.withdraw()

open_file = filedialog.askopenfilenames(filetypes=[("imagebyzaid", ".svg")])
file = open_file[0]
paths, attributes, svg_attributes = svg2paths2(file)

if len(paths) == 1:
    exit()

turtle.setworldcoordinates(0, 0, 500, 500)


def Vector(pathB):
    X1 = pathB[0].real
    Y1 = pathB[0].imag

    X2 = pathB[1].real
    Y2 = pathB[1].imag

    turtle.goto(X1,Y1)
    turtle.pendown()
    turtle.goto(X2,Y2)
    turtle.penup()

def Linear(x, y , t):
    return (x*(1-t)) + (y*t)

def Linear2(x, y,t):
    return Linear(x[0], y[0], t), Linear(x[1],y[1],t)

def Bezier(P0,P1,P2,P3, t):
    c1 = Linear2(P1,P2,t)
    c2 = Linear2(P0,c1,t)
    c3 = Linear2(c2, P3, t)
    c4 = Linear2(c2, c3, t)

    return c4

def BezierTurtle(P0,P1,P2,P3):
    t = 0
    while t < 1:
        t+= 0.001
        x,y = Bezier(P0,P1,P2,P3,t)
        if turtle.distance(x,y) >= 1:
            turtle.goto(x,y)
            turtle.pendown()



for l in range(len(paths)):
    bluepath = paths[l]
    for i in range(len(bluepath)):
        print(turtle.pos())
        turtle.penup()
        if isinstance(bluepath[i],Line):
            Vector(bluepath[i])
        else:
            P0 = (bluepath[i][0].real, bluepath[i][0].imag)
            P1 = (bluepath[i][1].real, bluepath[i][1].imag)
            P2 = (bluepath[i][2].real, bluepath[i][2].imag)
            P3 = (bluepath[i][3].real, bluepath[i][3].imag)
            BezierTurtle(P0,P1,P2,P3)
            turtle.penup()


turtle.done()

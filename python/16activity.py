import turtle
turtle.Screen().bgcolor("blue")
pen= turtle.Turtle()
# first triangle for star
for i in range(3):
    pen.forward(100)
    pen.left(120)
pen.penup()
pen.goto(0,60)
# second triangle for star
pen.pendown()
for i in range(3):
    pen.forward(100)
    pen.right (120)
pen.penup()
pen.goto(-100,120)
pen.pendown()
for i in range(5):
    pen.forward(100)
    pen.left(144)
turtle.done
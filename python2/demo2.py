import turtle
turtle.Screen().bgcolor("gray")

pen= turtle.Turtle()
pen.color("black")
pen.pensize(3)

for i in range(0,4):
    pen.forward(100)
    pen.right(90)

turtle.done()
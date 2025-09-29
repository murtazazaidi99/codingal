import turtle
# creating convas
Sc=turtle.Screen()
Sc.bgcolor('red')
Sc.setup(400,300)
# turtle.title("welcome to turtle window")
# turtle object creation
pen= turtle.Turtle()
# creating a square
for i in range(4):
    pen.forward(100)
    pen.left(90)
    i=i+1
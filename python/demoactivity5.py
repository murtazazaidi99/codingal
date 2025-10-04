import turtle
screen = turtle.Screen()
screen.title("Shapes - Triangle, Rectangle, Hexagon")
screen.bgcolor("yellow")
pen = turtle.Turtle()
pen.pensize(3)
# Function to draw polygon
def draw_polygon(sides, length, color):
    pen.color(color)
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
# Move turtle without drawing
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
 # Draw Rectangle
move(0, 0)
for i in range(2):
    pen.forward(150)   # length
    pen.left(90)
    pen.forward(100)   # width
    pen.left(90)
# Draw Equilateral Triangle
move(-200, 0)
draw_polygon(3, 100, "red")
# Draw Hexagon
move(200, 0)
draw_polygon(6, 70, "blue")
turtle.done()




# Ask the user to guess
# Computer chooses a random number between 1 and 10
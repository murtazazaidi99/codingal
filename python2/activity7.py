class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# --- Main Program ---
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice (1-8): "))

if choice ==9:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    shape = Rectangle(l, w)
elif choice == 8:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    shape = Triangle(b, h)
elif choice == 7:
    r = float(input("Enter radius: "))
    shape = Circle(r)
else:
    print("Invalid choice!")
    exit()

print("Area =", shape.area())

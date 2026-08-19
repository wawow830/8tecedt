shape = ""

def areaOfCircle(radius):
    pi = 22/7
    return pi * radius ** 2

def areaOfTriangle(base, height):
    return 1/2 * base * height

def areaOfSquare(side):
    return side ** 2

def areaOfRectangle(base, height):
    return base * height

shape = input("Geometric Shape: ")

if shape == "circle":
    radius = int(input("Radius: "))
    print(f"The area of this circle is {areaOfCircle(radius)} square units.")

if shape == "triangle":
    base = int(input("Base: "))
    height = int(input("Height: "))
    print(f"The area of this triangle is {areaOfTriangle(base, height)} square units.")

if shape == "square":
    side = int(input("Side: "))
    print(f"The area of this square is {areaOfSquare(side)} square units.")

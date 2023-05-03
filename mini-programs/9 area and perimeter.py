import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the area of a square
def square_area(side):
    return side ** 2

# Function to calculate the perimeter of a square
def square_perimeter(side):
    return 4 * side

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius

# Main program
print("Welcome to the Geometric Calculator!")
print("What shape do you want to calculate the area and perimeter for?")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is:", rectangle_area(length, width))
    print("The perimeter of the rectangle is:", rectangle_perimeter(length, width))
elif choice == "2":
    side = float(input("Enter the side length of the square: "))
    print("The area of the square is:", square_area(side))
    print("The perimeter of the square is:", square_perimeter(side))
elif choice == "3":
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle is:", circle_area(radius))
    print("The circumference of the circle is:", circle_circumference(radius))
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

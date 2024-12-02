import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        return "Radius cannot be negative."
    return math.pi * radius ** 2

def main():
    print("Circle Area Calculator")
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is: {area}")
    except ValueError:
        print("Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()

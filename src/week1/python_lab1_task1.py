"""
Task 1 Simple Function with Arithmetic


"""

import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = float(input("Enter the circle radius: "))
    area = circle_area(radius)
    print(f"The area of the circle is {area:.2f}")

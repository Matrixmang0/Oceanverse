import numpy as np

pi = np.pi

def circle_area(radius):
    """
    Calculate the area of a circle based on its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle, rounded to two decimal places.
    """
    area = pi * (radius ** 2)
    return round(area, 2)

# Example usage
print(circle_area(1))  # Output: 3.14
print(circle_area(5))  # Output: 78.54
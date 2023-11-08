# Circle Area Calculator

This Python script calculates the area of a circle based on its radius using the mathematical constant Pi (π).

## Table of Contents

- [Description](#description)
- [Usage](#usage)

## Description

The script includes a function called `circle_area(radius)` that calculates the area of a circle. It uses the formula for the area of a circle, which is π times the square of the radius.

## Function

### `circle_area(radius)`

- **Description:** Calculates the area of a circle.
- **Arguments:**
  - `radius` (float): The radius of the circle.
- **Returns:**
  - The area of the circle as a float, rounded to two decimal places.

## Usage

1. Open the script in your preferred Python environment or editor.

2. Modify the `radius` value with the desired radius of the circle.

3. Call the `circle_area(radius)` function with the updated radius.

4. The function will return the area of the circle, rounded to two decimal places.

```python
import numpy as np

pi = np.pi

def circle_area(radius):
  area = pi * (radius ** 2)
  return round(area, 2)

print(circle_area(1))  # Output: 3.14
print(circle_area(5))  # Output: 78.54
```

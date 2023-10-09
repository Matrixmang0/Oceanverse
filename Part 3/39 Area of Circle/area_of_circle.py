import numpy as np

pi = np.pi

def circle_area(radius):
  area = pi*(radius**2)
  return round(area, 2)

print(circle_area(1))
print(circle_area(5))
import numpy as np

up = np.array([(0, 1), (1, 0), (0, -1)])
down = -up
right = np.array([(1, 0), (0, 1), (-1, 0)])
left = -right

pattern = np.array([(1, 1)])

joint = np.array([(1, 0), (0, 1), (-1, 0), (0, -1)])

def sfc(n):  
  for _ in range(1, 2**n + 1):


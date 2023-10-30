import numpy as np

up = np.array([(0, 1), (1, 0), (0, -1)])
down = -up
right = np.array([(1, 0), (0, 1), (-1, 0)])
left = -right

pattern = np.array([(1, 1)])

def navigate(pattern, dir):
    if dir=='up':
      for tup in up:
        ne = pattern[-1] + tup
        pattern = np.append(pattern, ne)
    elif dir=='down':
      for tup in down:
        ne = pattern[-1] + tup
        pattern = np.append(pattern, ne)
    elif dir=='right':
      for tup in right:
        ne = pattern[-1] + tup
        pattern = np.append(pattern, ne)
    elif dir=='left':
      for tup in left:
        ne = pattern[-1] + tup
        pattern = np.append(pattern, ne)
    

def sfc(pattern, n):
  if n==0:
    return pattern
  elif n==1:
    return navigate(pattern, 'right')

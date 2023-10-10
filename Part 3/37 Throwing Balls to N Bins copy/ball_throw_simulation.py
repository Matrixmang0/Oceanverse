import random

def simulate_ball_throw(n_bins):

  bins = [0] * n_bins
  balls = 0

  while 0 in bins:
    bin_index = random.randint(0, n_bins-1)
    balls += 1
    bins[bin_index] += 1

  return balls

num_bins = int(input("Enter the number of bins : "))


num_balls_list = []
for i in range(1000):
  num_balls_list.append(simulate_ball_throw(num_bins))

max_occurred_balls= max(set(num_balls_list), key=num_balls_list.count)

print("The number of ball throws required is " + str(max_occurred_balls))

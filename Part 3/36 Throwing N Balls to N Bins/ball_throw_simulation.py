import random
import matplotlib.pyplot as plt

def simulate_ball_throw(n):

  bins = [0] * n
  for i in range(n):
    bin_index = random.randint(0, n-1)
    bins[bin_index] += 1

  max_balls = max(bins)
  return max_balls

count = int(input("Enter the number of balls and bins : "))


max_balls_list = []
for i in range(100):
  max_balls_list.append(simulate_ball_throw(count))

num_bins_hist = max(max_balls_list) - min(max_balls_list)

plt.hist(max_balls_list, bins=num_bins_hist, align='left', alpha=0.75, edgecolor='black' )
plt.title(f"Distribution of Maximum Balls in Bins (n={count})")
plt.xlabel("Maximum Balls in a Bin")
plt.xticks(range(min(max_balls_list), max(max_balls_list)+1))
plt.ylabel("Frequency")
plt.savefig('histogram.png')


def spiral_RULD():

  chars = ['R', 'U', 'L', 'D']

  string = ''
  num = 1
  iteration = 0

  while(len(string) <= 1_000_000):

    string += chars[iteration%len(chars)] * num
    if iteration%2!=0:
      num += 1
    iteration += 1


  return (string)

print(spiral_RULD())
def read_print_file(file):

  with open(file, 'r') as f :
    lines = f.readlines()
    for line in lines:
      print(line.strip())


read_print_file('input.txt')
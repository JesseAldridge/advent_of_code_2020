import os

def go():
  with open('2.txt') as f:
    text = f.read()

  valid_count = 0
  for line in text.splitlines():
    print('line:', line)
    pair, char, password = line.split()
    pair = [int(x) for x in pair.split('-')]
    required_char = char[0]
    count = 0
    if pair[0] - 1 < len(password) and password[pair[0] - 1] == required_char:
      count += 1
    if pair[1] - 1 < len(password) and password[pair[1] - 1] == required_char:
      count += 1
    if count == 1:
      print('valid')
      valid_count += 1
    else:
      print('invalid')
  print(valid_count)

go()

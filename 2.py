import os

def go():
  with open('2.txt') as f:
    text = f.read()

  valid_count = 0
  for line in text.splitlines():
    print('line:', line)
    bounds, char, password = line.split()
    bounds = [int(x) for x in bounds.split('-')]
    required_char = char[0]
    count = 0
    for ch in password:
      if ch == required_char:
        count += 1
    if count >= bounds[0] and count <= bounds[1]:
      print('valid')
      valid_count += 1
    else:
      print('invalid')
  print(valid_count)

go()

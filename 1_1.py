import os

def go():
  with open('1.txt') as f:
    text = f.read()

  nums = [int(line) for line in text.splitlines()]
  for num1 in nums:
    for num2 in nums:
        if num1 + num2 == 2020:
          print(num1, num2, num1 * num2)
          return
go()

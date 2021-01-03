
def binary_space_partition(min, max, sequence, index):
  print('min, max:', min, max, index, sequence)
  if min == max:
    return min
  if sequence[index] in ('F', 'L'):
    # (0 + 1) / 2 == 0
    # (0 + 3) / 2 == 1
    # (min + max) / 2 == greatest value in left partition == right - 1
    return binary_space_partition(min, (min+max)//2, sequence, index + 1)
  else:
    return binary_space_partition((min+max)//2 + 1, max, sequence, index + 1)

with open('5.txt') as f:
  lines = f.read().splitlines()

ids = []
for line in lines:
  print('line:', line)
  row = binary_space_partition(0, 127, line, 0)
  col = binary_space_partition(0, 7, line, 7)
  ids.append(row * 8 + col)

print('max id:', max(ids))
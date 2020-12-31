with open('3.txt') as f:
  mat = f.read().splitlines()

tree_count = 0
c = 0
for r, row in enumerate(mat):
  if mat[r][c] == '#':
    tree_count += 1
  c = (c + 3) % len(row)
print('tree count:', tree_count)

def count_trees(mat, r_delta, c_delta):
  tree_count = 0
  c = 0
  for r in range(0, len(mat), r_delta):
    if mat[r][c] == '#':
      tree_count += 1
    c = (c + c_delta) % len(mat[r])
  return tree_count

with open('3.txt') as f:
  mat = f.read().splitlines()

product = 1
for slope in [
  (1,1),
  (3,1),
  (5,1),
  (7,1),
  (1,2),
]:
  product *= count_trees(mat, slope[1], slope[0])
print('product:', product)

import os

with open('3.txt') as f:
    text = f.read()
map = []
for x in text.splitlines():
    map.append(x*100)
tree1 = 0
tree2 = 0
tree3 = 0
tree4 = 0
tree5 = 0
x_coordinate = 0
for line in map:
    if line[x_coordinate] == "#":
        tree1 += 1
    x_coordinate += 3
x_coordinate = 0
for line in map:
    if line[x_coordinate] == "#":
        tree2 += 1
    x_coordinate += 1
x_coordinate = 0
for line in map:
    if line[x_coordinate] == "#":
        tree3 += 1
    x_coordinate += 5
x_coordinate = 0
for line in map:
    if line[x_coordinate] == "#":
        tree4 += 1
    x_coordinate += 7
x_coordinate = 0
for item, line in enumerate(map):
    print(item % 2)
    if item % 2 == 0:
        if line[x_coordinate] == "#":
            tree5 += 1
        x_coordinate += 1
    # else:
    #     x_coordinate += 1
print(tree1*tree2*tree3*tree4*tree5)

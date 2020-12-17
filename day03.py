f = open('day03.txt')
map = [line.replace('\n', '') for line in f]
filename = 'day03.txt'


#down 1 right 3
for i in range(len(map)):
    tree_counter_1 = 0
    down = 1
    position_x = 0

    for position_y in range(0, len(map), down):
        if map[position_y][position_x] == "#":
            tree_counter_1 += 1
        position_x = (position_x + 3) % len(map[0])
print(tree_counter_1)

#down 1 right 1
for i in range(len(map)):
    tree_counter_2 = 0
    down = 1
    position_x = 0

    for position_y in range(0, len(map), down):
        if map[position_y][position_x] == "#":
            tree_counter_2 += 1
        position_x = (position_x + 1) % len(map[0])
print(tree_counter_2)
#down 1 right 5
for i in range(len(map)):
    tree_counter_3 = 0
    down = 1
    position_x = 0

    for position_y in range(0, len(map), down):
        if map[position_y][position_x] == "#":
            tree_counter_3 += 1
        position_x = (position_x + 5) % len(map[0])
print(tree_counter_3)
#down 1 right 7
for i in range(len(map)):
    tree_counter_4 = 0
    down = 1
    position_x = 0

    for position_y in range(0, len(map), down):
        if map[position_y][position_x] == "#":
            tree_counter_4 += 1
        position_x = (position_x + 7) % len(map[0])
print(tree_counter_4)
#down 2 right1
for i in range(len(map)):
    tree_counter_5 = 0
    down = 2
    position_x = 0

    for position_y in range(0, len(map), down):
        if map[position_y][position_x] == "#":
            tree_counter_5 += 1
        position_x = (position_x + 1) % len(map[0])
print(tree_counter_5)


tree_counter = 1
tree_counter = tree_counter * tree_counter_1
tree_counter = tree_counter *tree_counter_2
tree_counter = tree_counter * tree_counter_3
tree_counter = tree_counter * tree_counter_4
tree_counter = tree_counter * tree_counter_5
print(tree_counter)


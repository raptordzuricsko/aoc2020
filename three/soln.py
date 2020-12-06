def test():
    print('now running code')
    # load in input file
    with open('input.txt') as f:
        lines = f.read().splitlines()

    tree_count = 0
    # start at 1, 3
    x = 1
    y = 3
    while x < len(lines):
        if lines[x][y] == '#':
            tree_count += 1
        x += 1
        # meh, seems easier to jump to the front than extend matrices
        y = (y + 3) % len(lines[0])
    return tree_count


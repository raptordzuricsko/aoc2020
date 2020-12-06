def test():
    print('now running code')
    # load in input file
    with open('input.txt') as f:
        lines = f.read().splitlines()

    tree_counts = []
    # list of how many to move down, then how many to move right
    for pair in [[1,1], [1, 3], [1, 5], [1, 7], [2, 1]]:
        #start at the coordinates from the first pair, not 0,0
        x = pair[0]
        y = pair[1]
        tree_count = 0
        while x < len(lines):
            if lines[x][y] == '#':
                tree_count += 1
            x += pair[0]
            # meh, seems easier to jump to the front than extend matrices
            y = (y + pair[1]) % len(lines[0])
        tree_counts.append(tree_count)
    tree_multiplied_answer = 1
    for i in tree_counts:
        tree_multiplied_answer *= i
        
    return tree_multiplied_answer


def test():
    print('now running code')
    with open('input.txt') as f:
        lines = [int(x) for x in f.read().splitlines()]
    import pdb; pdb.set_trace()
    for x in lines:
        for y in lines:
            if x + y == 2020:
                print(x * y)
    print('test')
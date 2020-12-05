def test():
    print('now running code')
    with open('input.txt') as f:
        lines = [int(x) for x in f.read().splitlines()]
    import pdb; pdb.set_trace()
    for x in lines:
        for y in lines:
            for z in lines:
                if x + y + z == 2020:
                    print(x * y * z)
                    print(str(x) + ',' + str(y) + ',' + str(z))
    print('test')
def run():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        PREAMBLE_LEN = 25
    # with open('input2.txt') as f:
        # lines = f.read().splitlines()
        # PREAMBLE_LEN = 5

    # convert to numbers. looping again but whatever
    lines = [int(x) for x in lines]
    sum_lines = lines[:PREAMBLE_LEN]
    for i in range(PREAMBLE_LEN, len(lines)):
        is_it_the_sum = simple_check(sum_lines, lines[i])
        if not is_it_the_sum:
            print('wowee!')
            print(lines)
            print(sum_lines)
            print(lines[i])
            return lines[i]
        sum_lines.pop(0)
        sum_lines.append(lines[i])
        print(sum_lines)


def simple_check(lines, new_num):
    for i, line1 in enumerate(lines):
        for j, line2 in enumerate(lines[i:]):
            if (line1 + line2) == new_num:
                return True
    return False


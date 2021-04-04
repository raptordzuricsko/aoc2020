def run():
    # with open('input.txt') as f:
        # lines = f.read().splitlines()
        # PREAMBLE_LEN = 25
    with open('input2.txt') as f:
        lines = f.read().splitlines()
        PREAMBLE_LEN = 5

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

def run_p2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    # with open('input2.txt') as f:
        # lines = f.read().splitlines()
    # convert to numbers. looping again but whatever
    lines = [int(x) for x in lines]
    lowest, highest = p2_simple_check(lines)
    return lowest + highest

GOAL = 133015568
# GOAL = 127
def p2_simple_check(lines):
    for i, line1 in enumerate(lines):
        lowest_num = line1
        highest_num = line1
        sum = line1
        for j, line2 in enumerate(lines[i + 1:]):
            if (sum + line2) == GOAL:
                print('wowee!')
                print(i, j, line1, line2)
                print(lowest_num, highest_num)
                return lowest_num, highest_num
            elif (sum + line2) > GOAL:
                break
            if lowest_num > line2:
                lowest_num = line2
            if highest_num < line2:
                highest_num = line2
            sum += line2
    






# ans to pt1133015568
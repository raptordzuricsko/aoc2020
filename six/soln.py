
def test():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lines.append('')
    group_size = 0
    totals = []
    answers = [0] * 26
    # array of zeros
    for line in lines:
        if line == '':
            group_total = 0
            for i in answers:
                if i == group_size:
                    group_total += 1
            totals.append(group_total)

            # reset vals
            answers = [0] * 26
            group_size = 0
        else:
            for c in line:
                #convert a-z to 0-25
                answers[ord(c) - 97] += 1
            group_size += 1
    # print(total)
    sum = 0
    for val in totals:
        sum += val

    return sum
        

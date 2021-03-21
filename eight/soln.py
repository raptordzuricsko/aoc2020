
def run():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    instructions = []
    for i, line in enumerate(lines):
        line_parts = line.split(' ')
        op = line_parts[0]
        argument = line_parts[1]
        # and farther break apart argument into sign and val
        sign = argument[0]
        val = int(argument[1:])
        instructions.append({"op": op, "sign": sign, "val": val})



    # try to switch out the op
    for i, line in enumerate(instructions):
        switch(line)
        success, accumulator = try_with_instructions(instructions)
        if success:
            print(accumulator)
            breakpoint()
            return

        # switch it back. maybe confusing, could be more functional
        switch(line)

        




def try_with_instructions(lines):
    # stores whether the op has been done yet
    been_visited = [0] * len(lines)

    i = 0
    accumulator = 0
    ops = 0


    while i < len(lines):
        print(lines[i], i, accumulator)
        # exit condition is if the line has already been visited
        if been_visited[i]:
            return (False, accumulator)
        # mark that this op has been seen
        been_visited[i] = 1

        op = lines[i]['op']
        sign = lines[i]['sign']
        val = lines[i]['val']

        if op == 'nop':
            i += 1
        elif op == 'jmp':
            if sign == '-':
                i -= val
            elif sign == '+':
                i += val
            else:
                print('jmp parse failure:', i)
        elif op == 'acc':
            if sign == '-':
                accumulator -= val
            elif sign == '+':
                accumulator += val
            else:
                print('acc parse failure:', i)
            i += 1
        ops += 1
    return (True, accumulator)

    
def switch(line):
    if line["op"] == "nop":
        line["op"] = "jmp"
    elif line["op"] == "jmp":
        line["op"] = "nop"

        
        

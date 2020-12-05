def test():
    print('now running code')
    # load in input file
    with open('input.txt') as f:
        lines = f.read().splitlines()
        # do an initial parse, for kicks
        rules_and_usages = [x.replace(':','').split(' ') for x in lines]

    valid_password_count = 0
    for x in rules_and_usages:
        # set up variables
        min_and_max = x[0].split('-')
        min = int(min_and_max[0])
        max = int(min_and_max[1])
        tracked = x[1]
        password = x[2]

        # iterate
        tracked_count = 0
        for letter in password:
            if letter == tracked:
                tracked_count += 1

        # could be faster in the loop
        # check if the password meets the rules
        if tracked_count <= max and tracked_count >= min:
            valid_password_count += 1
            # import pdb; pdb.set_trace()
            # print('test"')
                
    return valid_password_count
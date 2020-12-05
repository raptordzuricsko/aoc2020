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
        rules = x[0].split('-')
        spot_one = int(rules[0]) - 1 # they indexed weird
        spot_two = int(rules[1]) - 1 # they indexed starting at one

        tracked = x[1]
        password = x[2]

        # iterate
        first_match = password[spot_one] == tracked
        second_match = password[spot_two] == tracked
        if (first_match and not second_match) or \
            (second_match and not first_match):
            valid_password_count += 1

            # import pdb; pdb.set_trace()
            # print('test"')
                
    return valid_password_count
def test():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        # make sure there's an extra space at the end 
        # so we can check the last passport
        lines.append('') 


    valid_pp_count = 0
    passports = []
    passport = {}

    for line in lines:
        # have we read in the whole passport?
        if line == '':
            # if so, figure out if it's valid
            valid_pp = validate_passport(passport)
            passports.append(passport.copy())
            if valid_pp:
                valid_pp_count += 1
            passport = {}

        else:
            # read in a line of qualities to a passport
            qualities = line.split(' ')
            for quality in qualities:
                q_k_p = quality.split(':')
                passport[q_k_p[0]] =  q_k_p[1]
        

    return valid_pp_count



required_qualities = ['byr', 'iyr', 'eyr', 'hgt',  
    'hcl', 'ecl', 'pid'] 
optional_qualities = ['cid']
def validate_passport(passport):
    for req_quality in required_qualities:
        if req_quality not in passport.keys():
            return False
    return True
        
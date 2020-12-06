def test():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        # make sure there's an extra space at the end 
        # so we can check the last passport
        lines.append('') 


    valid_pp_count = 0
    passports = []
    passport = {}
    valid_pps = []

    for line in lines:
        # have we read in the whole passport?
        if line == '':
            # if so, figure out if it's valid
            valid_pp = validate_passport(passport)
            passports.append(passport.copy())
            if valid_pp:
                valid_pp_count += 1
                valid_pps.append(passport.copy())
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

    try:
        if not (len(passport['byr']) == 4 and 
                int(passport['byr']) >= 1920 and 
                int(passport['byr']) <= 2002):
            return False
        if not (len(passport['iyr']) == 4 and 
                int(passport['iyr']) >= 2010 and 
                int(passport['iyr']) <= 2020):
            return False
        if not (len(passport['eyr']) == 4 and 
                int(passport['eyr']) >= 2020 and 
                int(passport['eyr']) <= 2030):
            return False

        #hgt validation
        if passport['hgt'].endswith('cm'):
            hgt = int(passport['hgt'].replace('cm',''))
            if not (hgt >= 150 and hgt <= 193):
                print('filtering out height!', hgt)
                return False
        elif passport['hgt'].endswith('in'):
            hgt = int(passport['hgt'].replace('in',''))
            if not (hgt >= 59 and hgt <= 76):
                print('filtering out height2!', hgt)
                return False
        else: return False

        #hcl validation #123def
        if len(passport['hcl']) != 7 or passport['hcl'][0] != '#':
            print('filtering out hcl', passport['hcl'])
            return False
        #check for hexadecimal >:)
        if not int(passport['hcl'][1:7], 16):
            print('filtering out hcl2', passport['hcl'])
            return False

        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if not (len(passport['pid']) == 9 or not int(passport['pid'])):
            return False
    except ValueError as e:
        print(e)
        return False
    return True
        
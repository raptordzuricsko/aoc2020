def main(): 
    with open('input.txt') as f:
        lines = f.read().splitlines()

    rules = {}

    for line in lines:
        rule = line.split(' bags contain ')
        defining_color = rule[0]
        suffixes = rule[1].split(', ')
        rules[defining_color] = {'rules' : [], 'eventually_contains_gold': False,}
        for suffix in suffixes:
            num_color_bags = suffix.split(' ')
            num = num_color_bags[0]
            color = ' '.join(num_color_bags[1:len(num_color_bags) - 1])
            # not needed
            # bags = num_color_bags[len(num_color_bags) - 1].strip('.')
            # print(f'num is {num}, color is {color}')
            rules[defining_color]['rules'].append({
                'num': num,
                'receiving_color': color
            })
        
        #rules should now look like 
        # 'posh_black' = {'rules': 
        # [{'num': '3', 'receiving_color': 'dark lavender'}, 
        # {'num': '3', 'receiving_color': 'mirrored coral'}, 
        # {'num': '1', 'receiving_color': 'dotted chartreuse'}]
        # }
    
    for key in rules.keys():
        populate_gold_contains(rules, key)

    keys = []
    for key in rules.keys():
        if rules[key]['eventually_contains_gold'] == True:
            keys.append(key)
    keys.sort()
    import pdb; pdb.set_trace()
    for key in keys:
        print(key)
        #mirrored white should definitely be true

    return len(keys)

def populate_gold_contains(rules, current_color):
    rule = rules[current_color]
    # if current_color == 'faded magenta':
        # print('magenta!')
        # import pdb; pdb.set_trace()
    for sub_rule in rule['rules']:
        if sub_rule['receiving_color'] == 'shiny gold':
            rule['eventually_contains_gold'] = True
            rule['gold_count'] = sub_rule['num'] 
            return True
            
    for sub_rule in rule['rules']:
        if sub_rule['num'] != 'no':
            rule['eventually_contains_gold'] = \
                populate_gold_contains(rules, sub_rule['receiving_color'])
    # if current_color == 'faded magenta':
        # print('magenta!')
        # import pdb; pdb.set_trace()
    for sub_rule in rule['rules']:
        if sub_rule['num'] != 'no' and rules[sub_rule['receiving_color']]['eventually_contains_gold'] == True:
            rule['eventually_contains_gold'] = True
            return True
    return False
    

        

            

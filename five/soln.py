def test():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    row_vals = []
    col_vals = []
    seat_ids = []
    for line in lines:
        row = [*range(0, 127 + 1)]
        column = [*range(0, 7 + 1)]
        for i in line:
            if i == 'F':
                row_mid = len(row) // 2
                row = row[:row_mid]
            if i == 'B':
                row_mid = len(row) // 2
                row = row[row_mid:]
            if i == 'L':
                col_mid = len(column) // 2
                column = column[:col_mid]
            if i == 'R':
                col_mid = len(column) // 2
                column = column[col_mid:]
        row_vals.append(row[0])
        col_vals.append(column[0])
        row_val = row[0]
        col_val = column[0]
        seat_id = ((row_val * 8) + col_val)
        seat_ids.append(seat_id)
        # col_vals.append(column[0])
  
    highest = 0 
    totals = []
    for i in range(0, len(row_vals)):
        total = row_vals[i] * 8 + col_vals[i]
        totals.append(total)
        if total > highest:
            highest = total


    seat_ids.sort()
    for i in range(0, len(seat_ids)):
        current = seat_ids[i]
        future = seat_ids[i + 1]
        if future != current + 1:
            return current + 1

def b_search_ugh(line, min, max):
    for i in range(0, len(line)):
        mid = int(min + (max - min) // 2)
        # import pdb; pdb.set_trace()
        # lower half
        if line[i] == 'F' or line[i] == 'L':
            max = mid - 1
        #  upper half
        elif line[i] == 'B' or line[i] == 'R':
            min = mid + 1
        print(min, max)
    return min

arr = []
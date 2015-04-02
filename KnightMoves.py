import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    position = test.strip()
    my_row = ord(position[0]) - 96
    my_col = int(position[1])
    rows = []
    cols = []
    valid_pos = []
    valid_range = range(1, 9)
    for i in range(1, 3):
        if (my_row + i) in valid_range:
            rows.append(chr(my_row + i + 96))
        if (my_row - i) in valid_range:
            rows.append(chr(my_row - i + 96))
        if i == 1:
            x = 2
        else:
            x = 1
        if (my_col + x) in valid_range:
            cols.append(my_col + x)
        if (my_col - x) in valid_range:
            cols.append(my_col - x)

        for r in rows:
            for c in cols:
                valid_pos.append('{}{}'.format(r, c))
        cols = []
        rows = []
    valid_pos.sort()
    print(' '.join(valid_pos))
test_cases.close()
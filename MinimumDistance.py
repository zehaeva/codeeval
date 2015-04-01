__author__ = 'zehaeva'

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_data = list(map(int, test.strip().split(' ')))
    num_of_houses = my_data[0]
    houses = my_data[1:]
    houses.sort()
    my_address = int(num_of_houses / 2)
    if num_of_houses % 2 != 0:
        my_house = houses[my_address]
    else:
        my_house = int((houses[my_address] + houses[my_address - 1]) / 2)
    total_distance = 0
    for x in houses:
        total_distance += abs(x - my_house)
    print(total_distance)

test_cases.close()
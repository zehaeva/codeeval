def dim_list(num):
    return [[0 for x in range(num)] for x in range(num)]


def reverse_list(l, dim):
    new_list = dim_list(dim)
    for x in range(0, dim):
        new_list[x] = l[x][::-1]
    return new_list


import sys
import math
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    raw_list = test.strip().split(' ')
    dimension = int(math.sqrt(len(raw_list)))
    my_list = dim_list(dimension)
    counter = 0
    for x in range(dimension):
        for y in range(dimension):
            my_list[x][y] = raw_list[counter]
            counter += 1
    rotated = reverse_list([list(x) for x in zip(*my_list)], dimension)
    myreturn = [' '.join(x) for x in rotated]
    print(' '.join(myreturn))

test_cases.close()
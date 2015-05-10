__author__ = 'zehaeva'

import sys


def bubble_sort(my_list):
    length = len(my_list)
    for i in range(0, length - 1):
        if my_list[i] > my_list[i + 1]:
            hold = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = hold

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    temp = test.strip().split('|')
    my_list = [int(x) for x in temp[0].strip().split(' ')]
    interrupt = int(temp[1])
    counter = 0
    # max time to execute
    if interrupt > len(my_list) ** 2:
        interrupt = len(my_list) ** 2
    while counter < interrupt:
        counter += 1
        bubble_sort(my_list)
    my_list = [str(x) for x in my_list]
    print(' '.join(my_list))
test_cases.close()
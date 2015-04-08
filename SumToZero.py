__author__ = 'zehaeva'

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ['2,3,1,0,-4,-1', '0,-1,3,-2']
for test in test_cases:
    my_list = [int(x) for x in test.strip().split(',')]
    my_count = 0
    for w in range(0, len(my_list) - 3):
        for x in range(w + 1, len(my_list)):
            for y in range(x + 1, len(my_list)):
                for z in range(y + 1, len(my_list)):
                    if (my_list[x] + my_list[w] + my_list[y] + my_list[z]) == 0:
                        my_count += 1
    print(my_count)
test_cases.close()
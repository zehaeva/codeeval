import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = [int(x) for x in test.replace('\n', '').split(',')]
    length = len(my_list)
    largest = [0, 1]
    for left in range(0, length):
        for right in range(length, left, -1):
            if sum(my_list[left:right]) > sum(my_list[largest[0]:largest[1]]):
                largest[0] = left
                largest[1] = right
    print('{}'.format(sum(my_list[largest[0]:largest[1]])))

test_cases.close()
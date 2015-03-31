import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = [int(x) for x in test.replace('\n', '').split(',')]
    my_return = []
    for x in my_list:
        if not x in my_return:
            my_return.append(x)
    my_return.sort()
    my_return = [str(x) for x in my_return]
    print(','.join(my_return))

test_cases.close()
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = [float(x) for x in test.replace('\n','').split(' ')]
    my_list.sort()
    print(' '.join(['{:0.3f}'.format(x) for x in my_list]))

test_cases.close()
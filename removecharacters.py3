import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = test.replace('\n', '').split(',')
    for x in my_list[1].strip(' '):
        my_list[0] = my_list[0].replace(x, '')
    print(my_list[0].rstrip(' '))
test_cases.close()
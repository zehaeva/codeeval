import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_return = 0
    for i in test.replace('\n', ''):
        my_return += int(i)
    print(my_return)
    
test_cases.close()
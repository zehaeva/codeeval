import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print('{0:b}'.format(int(test.strip)))

test_cases.close()
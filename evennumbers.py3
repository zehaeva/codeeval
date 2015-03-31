import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_val = int(test[-2:-1])
    if my_val % 2 == 0:
        print(1)
    else:
        print(0)

test_cases.close()
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_number = test.strip()
    self_describing = 1
    for i in range(0, len(my_number)):
        if my_number[i:i+1] != str(my_number.count(str(i))):
            self_describing = 0
            break
    print(self_describing)
test_cases.close()
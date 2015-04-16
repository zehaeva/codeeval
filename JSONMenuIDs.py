import re
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = re.findall('{["a-zA-Z :0-9,]+}', test)
    total = 0
    for x in my_list:
        if 'label' in x:
            total += int(re.findall('"id": ([0-9]+)', x)[0])
    print(total)
test_cases.close()
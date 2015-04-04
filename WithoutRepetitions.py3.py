__author__ = 'zehaeva'

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myreturn = list()
    myreturn.append(test[0])
    for x in range(1, len(test) - 1):
        if test[x - 1] != test[x]:
            myreturn.append(test[x])
    print(''.join(myreturn))
test_cases.close()
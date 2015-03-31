import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist = test.split(',')
    found = False
    i = 0
    while not found:
        i += 1
        if int(mylist[0]) <= (int(mylist[1]) * i):
            found = True
    print((int(mylist[1]) * i))

test_cases.close()
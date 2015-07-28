import sys, string
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist = ''.join(sorted(test.strip().replace(' ', '').lower()))
    sums = {}
    finalsum = 0
    for x in string.ascii_lowercase:
        sums[x] = 0
    for x in mylist:
        if x in string.ascii_lowercase:
            sums[x] += 1
    count = len(sums)
    for i in range(26, 0, -1):
        mymax = 0
        maxkey = ''
        for key, value in sums.items():
            if mymax < value:
                maxkey = key
                mymax = value
        if maxkey != '':
            finalsum += i * sums[maxkey]
            sums[maxkey] = 0
    print(finalsum)
test_cases.close()

import sys
test_cases = open(sys.argv[1], 'r')
x = 0
for test in test_cases:
    x += int(test.replace('\n','')) 
print(x)

test_cases.close()
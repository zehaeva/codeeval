import string
import sys
#test_cases = ['A quick brown fox jumps over the lazy dog', 'A slow yellow fox crawls under the proactive dog']
lowers = string.ascii_lowercase
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.lower().strip()
    letters = []
    for x in lowers:
        if x not in test:
            letters.append(x)
    if len(letters) == 0:
        print('NULL')
    else:
        letters.sort()
        print(''.join(letters))

test_cases.close()
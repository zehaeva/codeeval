import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	words = test.strip().split(' ')
	returnwords = []
	for word in words:
		returnwords.append(word[-1] + word[1:-1] + word[0:1])
	print(' '.join(returnwords))
test_cases.close()
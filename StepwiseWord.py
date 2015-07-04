import sys 

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	words = test.split(' ')
	longest = ''
	for word in words:
		if len(longest) < len(word):
			longest = word
	x = ''
	newword = []
	for letter in longest:
		newword.append(x + letter)
		x += '*'

	print(' '.join(newword))
test_cases.close()
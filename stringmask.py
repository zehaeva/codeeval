import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	my_test = test.split(' ')
	myreturn = ''
	for i in range(0, len(my_test[0])):
		if my_test[1][i] == '1':
			myreturn = '{}{}'.format(myreturn, my_test[0][i].upper())
		else:
			myreturn = '{}{}'.format(myreturn, my_test[0][i])
	print(myreturn)
test_cases.close()
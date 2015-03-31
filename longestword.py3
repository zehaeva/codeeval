import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = test.replace('\n','').split(' ')
    longest_word = ''
    for i in my_list:
        if len(i) > len(longest_word):
            longest_word = i
    print(longest_word)
test_cases.close()
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = test.replace('\n', '').split(' ')
    my_index = int(my_list[len(my_list) - 1])
    if (my_index + 1) <= len(my_list):
        print(my_list[len(my_list) - 1 - my_index])
test_cases.close()
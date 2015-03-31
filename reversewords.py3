import sys

def reverse_word(my_string):
    string_list = my_string.rsplit(' ', 1)
    if len(string_list) == 2:
        my_return = string_list[1] + ' ' + reverse_word(string_list[0])
    else:
        my_return = my_string
    return my_return

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(reverse_word(test.replace('\n', '').replace('\r', '')))

test_cases.close()
import sys
def am_i_happy(my_number, seen):
    y = 0
    for x in str(my_number):
        y += int(x) * int(x)
    if y == 1:
        my_return = 1
    elif y in seen:
        my_return = 0
    else:
        seen.append(y)
        my_return = am_i_happy(y, seen)
    return my_return
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = test.strip()
    seen = []
    print(am_i_happy(my_list, seen))
test_cases.close()
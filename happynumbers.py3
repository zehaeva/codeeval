import sys
def am_i_happy(my_number, seen):
    y = sum(map(lambda x : int(x) ** 2, str(my_number)))
    if y in [1,10,100,13,31,130,103]:
        my_return = 1
    elif y in seen or len(seen) > 3:
        my_return = 0
    else:
        seen.append(y)
        my_return = am_i_happy(y, seen)
    return my_return
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(am_i_happy(test.strip(), []))
test_cases.close()
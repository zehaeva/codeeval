__author__ = 'zehaeva'
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_number = test.strip()
    counter = 0
    half = int(len(my_number) / 2)
    if len(my_number) % 2 == 0:
        half_r = half - 1
    else:
        half_r = half
    while my_number[:half] != my_number[:half_r:-1]:
        counter += 1
        my_reverse = my_number[::-1]
        my_number = str(int(my_number) + int(my_reverse))
        half = int(len(my_number) / 2)
        if len(my_number) % 2 == 0:
            half_r = half - 1
        else:
            half_r = half
        if counter > 100:
            break
    print('{} {}'.format(counter, my_number))
test_cases.close()
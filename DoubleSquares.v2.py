__author__ = 'zehaeva'

import math

test_cases = ['20', '100']
test_cases = ['100', '20', '801125', '2147302922', '412585807', '522585645', '533491805', '366212969', '662700292', '411363534', '893117564', '469501161', '469030068', '840864434', '553374335', '703137330', '850602692', '959833476', '262816515', '609921782', '837179264', '298009996', '29641625', '1215306625']

all_squares = set()
all_squares.add(0)
max_num = int(math.sqrt(2147483647))
for i in range(1, max_num):
    all_squares.add(i**2)

number_of_cases = None
for test in test_cases:
    test = int(test)
    if number_of_cases is None:
        number_of_cases = test
    else:
        found_counter = 0
        max_test = test
        for i in all_squares:
            remainder = test - i
            if remainder in all_squares:
                found_counter += 1
        print(int(found_counter/2))
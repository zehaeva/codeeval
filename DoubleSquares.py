import sys
import math
test_cases = open(sys.argv[1], 'r')

number_of_cases = None
for test in test_cases:
    num = int(test.strip())
    if number_of_cases is None:
        number_of_cases = num
    else:
        max_square = int(math.sqrt(num)) + 1
        counter = 0
        for x in range(0, max_square):
            remainder = math.sqrt(num - x**2)
            if remainder - int(remainder) == 0:
                counter += 1
        print(int(counter/2))
test_cases.close()
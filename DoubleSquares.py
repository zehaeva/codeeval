import sys
import math

test_cases = open(sys.argv[1], 'r')
number_of_cases = None
for test in test_cases:
    num = int(test.strip())
    if number_of_cases is None:
        number_of_cases = num
    else:
        max_square = int(math.sqrt(num))
        counter = 0
        for x in range(0, max_square):
            my_square = x**2
            if my_square > num / 2:
                break
            else:
                remainder = math.sqrt(num - my_square)
                if remainder - int(remainder) == 0:
                    counter += 1
        print(int(counter))
test_cases.close()
import sys
def fib(n):
    if n <= 0:
        my_return = 0
    elif n == 1:
        my_return = 1
    else:
        n_one = fib(n-1)
        n_two = fib(n-2)
        my_return = n_one + n_two
    return my_return
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n = int(test.replace('\n',''))
    print(fib(n))

test_cases.close()

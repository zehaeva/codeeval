import sys

def prime_sieve(min_num, max_num):
    if min_num < 2 and max_num < 2:
        primes = []
    else:
        if min_num % 2 == 0:
            min_num += 1
        elif min_num < 3:
            min_num = 3

    #how to sieve for primes
    #get all the numbers first
        pool = list(range(min_num, max_num, 2))
        primes = clean_pool(pool, max_num)
        primes.append(2)
    #if that number is in the pool, remove it
    primes.sort()
    return primes

def clean_pool(pool, max_value):
    #then take the first number
    new_prime = pool[0]
    if new_prime * new_prime < max_value:
        #and multiply it by the other numbers that are left
        last_index = 0
        pool_length = len(pool)
        delete = [False] * pool_length
        delete[0] = True
        for i in range(0, pool_length):
            x = pool[i]
            y = x * new_prime
            if y < max_value:
                for j in range(last_index, pool_length):
                    if y == pool[j]:
                        delete[j] = True
                        last_index = j
                        break
            else:
                break
        drain_pool = []
        for i in range(0, pool_length):
            if not delete[i]:
                drain_pool.append(pool[i])
        #then call us again with what's left
        primes = clean_pool(drain_pool, max_value)
        primes.append(new_prime)
    else:
        primes = pool
    return primes


test_cases = open(sys.argv[1], 'r')

my_values = []

for test in test_cases:
    my_values.append(int(test.replace('\n', '')))

my_test = max(my_values)
#my_primes = calc_primes(my_test)
my_primes = prime_sieve(1, my_test)

for v in my_values:
    print_primes = []
    for x in my_primes:
        if x < v:
            print_primes.append(x)

    my_return = [str(x) for x in print_primes]
    print(','.join(my_return))

test_cases.close()
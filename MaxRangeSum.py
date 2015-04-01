import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = test.replace('\n', '').split(';')
    num_days = int(my_list[0])
    stock = [int(x) for x in my_list[1].split(' ')]
    max_value = -90000000
    mylength = len(stock) - num_days + 1
    for i in range(0, mylength):
        mysum = sum(stock[i:i+num_days])
        if max_value < mysum:
            max_value = mysum
    if max_value < 0:
        max_value = 0
    print(max_value)

test_cases.close()
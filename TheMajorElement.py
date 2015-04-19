import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list = [int(x) for x in test.strip().split(',')]
    my_list.sort()
    l = len(my_list)
    major_l = int(l / 2)
    answer = "None"
    for i in range(0, major_l):
        if my_list[i] == my_list[major_l + i]:
            answer = my_list[i]
            break
    print(answer)
test_cases.close()

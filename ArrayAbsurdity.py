__author__ = 'zehaeva'

test_cases = ['5;0,1,2,3,0', '20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14']

for test in test_cases:
    my_test = test.strip().split(';')
    my_n = my_test[0]
    my_list = my_test[1].split(',')
    my_list.sort()
    last_seen = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] == last_seen:
            break
        else:
            last_seen = my_list[i]
    print(last_seen)
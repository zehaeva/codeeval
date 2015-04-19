__author__ = 'zehaeva'
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_points = [int(x) for x in test.strip().split(' ')]
    direction = ''

    if my_points[1] == my_points[3] and my_points[0] == my_points[2]:
        direction = 'here'

    if my_points[1] < my_points[3]:
        direction += 'N'
    elif my_points[1] > my_points[3]:
        direction += 'S'

    if my_points[0] < my_points[2]:
        direction += 'E'
    elif my_points[0] > my_points[2]:
        direction += 'W'

    print(direction)

test_cases.close()
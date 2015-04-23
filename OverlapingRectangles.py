__author__ = 'zehaeva'

import sys

test_cases = open(sys.argv[1], 'r')

def inside_test(b1, b2):
    inside_x = False
    inside_y = False
    for p in b2:
        if b1[0][0] <= p[0] <= b1[1][0]:
            inside_x = True
        if b1[0][1] >= p[1] >= b1[1][1]:
            inside_y = True
    for p in b1:
        if b2[0][0] <= p[0] <= b2[1][0]:
            inside_x = True
        if b2[0][1] >= p[1] >= b2[1][1]:
            inside_y = True

    if inside_x and inside_y:
        return True
    else:
        return False


def shift_rectangles(rectangles):
    for y in range(0, 2):
        min_val = 0
        for x in range(y, len(rectangles), 2):
            if min_val > rectangles[x]:
                min_val = rectangles[x]

        shift_val = abs(min_val)
        for x in range(y, len(rectangles), 2):
            rectangles[x] += shift_val

    return rectangles

for test in test_cases:
    my_rectangles = [int(x) for x in test.strip().split(',')]
    my_rectangles = shift_rectangles(my_rectangles)

    rect_ichi = [(my_rectangles[0], my_rectangles[1]), (my_rectangles[2], my_rectangles[3])]
    rect_ni = [(my_rectangles[4], my_rectangles[5]), (my_rectangles[6], my_rectangles[7])]

    print('{}'.format(inside_test(rect_ichi, rect_ni)))
test_cases.close()
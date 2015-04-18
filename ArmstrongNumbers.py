import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ['6', '153', '351']
for test in test_cases:
    am_i_strong = test.strip()
    digits = [int(x) for x in am_i_strong]
    n = len(digits)
    total = 0
    for x in digits:
        total += x ** n
    if total == int(am_i_strong):
        print("True")
    else:
        print("False")

test_cases.close()
import sys
import string
chars = string.ascii_letters
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myreturn = []
    cap = True
    for i in range(0, len(test)):
        if test[i] in chars:
            if cap:
                myreturn.append(test[i].upper())
                cap = False
            else:
                myreturn.append(test[i].lower())
                cap = True
        else:
            myreturn.append(test[i])
    print(''.join(myreturn))
test_cases.close()
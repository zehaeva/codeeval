import re
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(re.sub(r"[A-Za-z0-9]+(['!@#$%^&*\(\)A-Za-z0-9]+)?", lambda am: am.group(0)[0].upper() + am.group(0)[1:], test))

test_cases.close()
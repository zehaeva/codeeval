class Romans():
    holder = {}

    def __init__(self):
        self.holder['M'] = 1000
        self.holder['D'] = 500
        self.holder['C'] = 100
        self.holder['L'] = 50
        self.holder['X'] = 10
        self.holder['V'] = 5
        self.holder['I'] = 1

    def __getitem__(self, item):
        return self.holder[item]

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ['3M1D2C', '2I3I2X9V1X', '3X2I4X', '1C2M']
for test in test_cases:
    source = test.strip()
    romans = Romans()
    adding = []
    subtracting = []
    for x in range(0, len(source), 2):
        if (x + 3) <= len(source):
            if romans[source[x + 1]] < romans[source[x + 3]]:
                subtracting.append(romans[source[x + 1]] * int(source[x]))
            else:
                adding.append(romans[source[x + 1]] * int(source[x]))
        else:
            adding.append(romans[source[x + 1]] * int(source[x]))
        last_r = romans[source[x + 1]]
    print(sum(adding) - sum(subtracting))

test_cases.close()
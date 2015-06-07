import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    times = test.strip().split(' ')
    #convert to seconds
    seconds = []
    for time in times:
        values = [int(x) for x in time.split(':')]
        seconds.append(values[0] * (60**2) + values[1] * 60 + values[2])
        
    result = abs(seconds[0] - seconds[1])
    
    hours = int(result / (60**2))
    minutes = int((result - (hours * (60**2))) / 60)
    seconds = int(result - (hours * (60**2)) - (minutes * 60))

    print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

test_cases.close()

found_list = []

#no even numbers
i = 1
found_list.append(2)
#for i in range(3, 1000, 2):
while len(found_list) < 1000:
    i += 2
    #can't be modulus-able by 3, that's easy
    found = False
    for x in found_list:
        if i % x == 0:
            found = True
            break
    if not found:
        found_list.append(i)
print(sum(found_list))
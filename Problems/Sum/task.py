# read sums.txt

test_file = open('sums.txt')
for line in test_file:
    total = 0
    values = line.split(' ')
    for value in values:
        total += int(value)
    print(total)

test_file.close()

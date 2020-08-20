# read sample.txt and print the number of lines
# read sums.txt

test_file = open('sample.txt')
# for line in test_file.readlines():
#     total = 0
#     values = line.split(' ')
#     for value in values:
#         total += int(value)
#     print(total)
print(len(test_file.readlines()))
test_file.close()

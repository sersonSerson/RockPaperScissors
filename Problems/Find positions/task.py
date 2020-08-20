numbers_list = '5 8 2 7 8 8 2 4'.split()
find_number = '8'
# # numbers_list = '5 10 2 7 8 8 2 4'.split()
# # find_number = '10'
# numbers_list, find_number = input().split(), input()

# indexes = [str(i) for i in range(len(numbers_list))
#            if find_number == numbers_list[i]]


# for i in range(len(numbers_list)):
#     if find_number == numbers_list[i]:
#         indexes.append(str(i))

# if len(indexes) == 0:
#     positions = 'not found'
# else:
#     positions = ' '.join(indexes)

# indexes = [str(i) for i in range(len(numbers_list))
#            if find_number == numbers_list[i]]
# print(' '.join(indexes) if len(indexes) > 0 else 'not found')


print([i for i in range(1, 10) if i > 3])

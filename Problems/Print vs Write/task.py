numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_new = open('file_with_list.txt', mode='w')
print((numbers), end='', file=file_new)
# file_old = open('animals.txt', mode='r', encoding='utf-8')
# for line in file_old:
#     file_new.write(line.replace('\n', '') + ' ')
file_new.close()
# file_old.close()

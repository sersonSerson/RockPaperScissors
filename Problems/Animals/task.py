# read animals.txt
# and write animals_new.txt

# file_new = open('animals_new.txt', mode='w', encoding='utf-8')
# file_old = open('animals.txt', mode='r', encoding='utf-8')
# for line in file_old:
#     file_new.write(line.replace('\n', '') + ' ')
# file_new.close()
# file_old.close()

text_file = open('text_file.txt', mode='w')                              # 1
print('The specified string to be written', file=text_file)  # 2
text_file.close()

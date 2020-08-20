# sentence = input()
# sentence = 'First ladies rule the State and state ' \
#            'the rule: ladies first'
# list_of_words = sentence.split()
# new_list = list()
# for word in list_of_words:
#     if word[-1] == 's':
#         new_list.append(word)
#
# print('_'.join(new_list))

print('_'.join((w for w in input().split() if w.endswith('s'))))


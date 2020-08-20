# phrase = 'BIRD'
# phrase = 'my_class'
# phrase = input()
# phrase_list = phrase.lower().split('_')
# for CapWords in phrase.lower().split('_'):
#     print(CapWords[0].upper() + CapWords[1:], end='')

print("".join(i.capitalize() for i in input().split('_')))

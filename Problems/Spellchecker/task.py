dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

checked = input().split()
# checked = 'srutinize is to examene closely and minutely'.split()
# checked = 'all correct'.split()
output = '\n'.join([i for i in checked if i not in dictionary])
print(output if len(output) > 0 else 'OK')

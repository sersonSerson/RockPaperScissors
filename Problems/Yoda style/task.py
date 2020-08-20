import random

# your sentence is assigned to the variable
sentence = input().split()
# sentence = "Luke, I'm your father"
# sentence = sentence.split()
# write your python code below
random.seed(43)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))

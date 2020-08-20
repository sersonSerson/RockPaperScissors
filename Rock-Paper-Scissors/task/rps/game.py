import random


def winner(user, computer):
    global score
    if user in variants[computer]:
        print(f'Sorry, but computer chose {computer}')
    elif user == computer:
        print(f'There is a draw ({computer})')
        score += 50
    elif computer in variants[user]:
        print(f'Well done. Computer chose {computer} and failed ')
        score += 100


def rating_file(mode):
    return open('rating.txt', mode=mode)


def user_score(login):
    found_player = False

    file = rating_file('r')
    for i in file:
        player = i.split(' ')[0]
        if player == login:
            found_player = True
            score = int(i.split(' ')[1])
    file.close()

    if not found_player:
        score = 0

    return score


login = input('Enter your name:')
print(f'Hello, {login}')
score = user_score(login)
variants = input()
# variants = ''
if variants == '':
    variants = 'scissors,rock,paper'

variants_list = variants.split(',')
total_variants = int((len(variants_list) - 1) / 2)

variants = dict()
for variant in variants_list:
    list_of_variants = list()
    # Variants after
    for i in variants_list[variants_list.index(variant) + 1:]:
        list_of_variants.append(i)
    # Variants before
    for i in variants_list[:variants_list.index(variant)]:
        list_of_variants.append(i)

    variants[variant] = ''.join(list_of_variants[total_variants:])

print("Okay, let's start")

user = input()
while user != '!exit':

    if user in variants:
        computer = random.choice(list(variants))
        winner(user, computer)
    elif user == '!rating':
        print(f'Your rating: {score}')
    else:
        print('Invalid input')

    user = input()
else:
    print('Bye!')


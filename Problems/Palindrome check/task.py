# please work with the preset variable `word`
# word = 'laptop'
forward = word
backward = word[::-1]

if forward == backward:
    print("Yes")
else:
    print("No")

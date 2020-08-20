phrase = input().split()
# phrase = 'lower camel case'.split()
print(phrase[0] + "".join(word.capitalize() for word in phrase[1:]))

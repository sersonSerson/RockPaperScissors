text = input()
# text = 'WWW.GOOGLE.COM uses 100-percent renewable energy sources ' \
#        'and www.ecosia.com plants a tree for every 45 searches!'

# text = text.lower()
words = text.split()

site_prefixes = ['https://', 'http://', 'www.']

for word in words:
    for prefix in site_prefixes:
        if word.startswith(prefix) or word.startswith(prefix.upper()):
            print(word)

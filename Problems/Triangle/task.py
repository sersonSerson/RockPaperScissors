height = int(input())
# height = 10
# for i in range(1, height + 1):
print("\n".join([('#' * int(i * 2 - 1)).center(height * 2 - 1) for i in range(1, height + 1)]))

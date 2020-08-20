# write your code here
with open('salary.txt', 'r') as salary:
    with open('salary_year.txt', 'w') as salary_year:
        for line in salary:
            print(str(int(line) * 12), file=salary_year)

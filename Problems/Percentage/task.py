def get_percentage(number, round_digits='none'):
    percentage = number * 100
    percentage = int(percentage) if round_digits == 'none' else round(percentage, round_digits)
    return f'{percentage}%'


# print(get_percentage(0.0123) == '1%')      # '1%'
# print(get_percentage(0.0123, 0) == '1.0%')   # 1.0%
# print(get_percentage(0.0123, 1) == '1.2%')   # 1.2%
# print(get_percentage(0.0123, 10) == '1.23%')  # 1.23%

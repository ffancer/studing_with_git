def get_sum_of_digits(num):
    sum = 0
    digits = str(num)
    for x in digits:
        sum += int(x)
    return sum


print(get_sum_of_digits(123), 6)

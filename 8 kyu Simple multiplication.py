def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


print(simple_multiplication(2), 16)
print(simple_multiplication(1), 9)
print(simple_multiplication(8), 64)
print(simple_multiplication(4), 32)
print(simple_multiplication(5), 45)

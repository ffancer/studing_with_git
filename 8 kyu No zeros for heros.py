def no_boring_zeros(n):
    n = str(n)
    print(len(n) - len(n.rstrip('0')))


print(no_boring_zeros(1450), 145)
print(no_boring_zeros(960000), 96)
print(no_boring_zeros(1050), 105)
print(no_boring_zeros(-1050), -105)
print(no_boring_zeros(0), 0)
print(no_boring_zeros(2016), 2016)

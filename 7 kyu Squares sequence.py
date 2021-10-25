def squares(x, n):
    lst = []

    for i in range(n):
        lst.append(x)
        x **= 2

    return lst

print(squares(2, 5), [2, 4, 16, 256, 65536])
print(squares(3, 3), [3, 9, 81])
print(squares(5, 3), [5, 25, 625])
print(squares(10, 4), [10, 100, 10000, 100000000])
print(squares(2, 0), [])
print(squares(2, -4), [])
def evil(n):
    return "It's Evil!" if bin(n).count('1') % 2 == 0 else "It's Odious!"


print(evil(1), "It's Odious!")
print(evil(2), "It's Odious!")
print(evil(3), "It's Evil!")

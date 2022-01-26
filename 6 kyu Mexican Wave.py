def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i] != ' ']

print(wave("hello"))
print(wave("codewars"))
print(wave(""))
print(wave("two words"))
print(wave(" gap "))
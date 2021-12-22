def find_smallest(numbers, to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))

print(find_smallest([5, 4, 3, 2, 1], "value"), 1)
print(find_smallest([5, 4, 3, 2, 1], "index"), 4)
print(find_smallest([8, 0, 9], "index"), 1)
print(find_smallest([8, 0, 9], "value"), 0)
print(find_smallest([1, 1, 0, 0, 1, 1], "value"), 0)
print(find_smallest([1, 1, 0, 0, 1, 1], "index"), 2)

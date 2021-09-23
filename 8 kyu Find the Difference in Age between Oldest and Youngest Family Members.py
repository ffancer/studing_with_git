def difference_in_ages(ages):
    return min(ages), max(ages), max(ages) - min(ages)


print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]), (3, 88, 85))
print(difference_in_ages([5, 8, 72, 98, 41, 16, 55]), (5, 98, 93))
print(difference_in_ages([57, 99, 14, 32]), (14, 99, 85))
print(difference_in_ages([62, 0, 3, 77, 88, 102, 26, 44, 55]), (0, 102, 102))
print(difference_in_ages([2, 44, 34, 67, 88, 76, 31, 67]), (2, 88, 86))
print(difference_in_ages([46, 86, 33, 29, 87, 47, 28, 12, 1, 4, 78, 92]), (1, 92, 91))
print(difference_in_ages([66, 73, 88, 24, 36, 65, 5]), (5, 88, 83))
print(difference_in_ages([12, 76, 49, 37, 29, 17, 3, 65, 84, 38]), (3, 84, 81))
print(difference_in_ages([0, 110]), (0, 110, 110))
print(difference_in_ages([33, 33, 33]), (33, 33, 0))

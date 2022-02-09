def solution(n, d):
    if d < 1:
        return []

    lst = []

    for i in str(n % 10 ** d):
        lst.append(int(i))

    return lst



print(solution(1, 1), [1])
print(solution(123767, 4), [3, 7, 6, 7])
print(solution(0, 1), [0])
print(solution(34625647867585, 10), [5, 6, 4, 7, 8, 6, 7, 5, 8, 5])
print(solution(1234, 0), [])
print(solution(24134, -4), [])
print(solution(1343, 5), [1, 3, 4, 3])

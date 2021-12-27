def solution(stones):
    return sum(1 for i in range(len(stones) - 1) if stones[i] == stones[i + 1])

print(solution("RGBRGBRGGB"), 1)
print(solution("RGGRGBBRGRR"), 3)
print(solution("RRRRGGGGBBBB"), 9)

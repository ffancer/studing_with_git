def delete_nth(order, max_e):
    ans = []

    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans


print(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])

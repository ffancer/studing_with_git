def pillars(num_pill, dist, width):
    return (num_pill - 1) * dist * 100 + (num_pill - 2) * width


print(pillars(1, 10, 10), 0)
print(pillars(2, 20, 25), 2000)
print(pillars(11, 15, 30), 15270)

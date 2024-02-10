def rolling_avg(a):
    return list(filter(bool, map(lambda x: round(sum([a[a.index(x) + i] for i in range(3) if a.index(x) + 2 <= len(a) - 1]) / 3, 2), a)))


print(rolling_avg([2,3,45,6,7,9]))
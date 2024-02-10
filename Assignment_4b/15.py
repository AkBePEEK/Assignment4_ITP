def perf_sqr(a):
    return list(filter(lambda x: x == int(x ** 0.5) ** 2, a))


print(perf_sqr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16]))
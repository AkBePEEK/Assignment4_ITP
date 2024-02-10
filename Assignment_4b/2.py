def even(a):
    return list(filter(lambda x: x%2==0, a))


print(even([1, 2, 3, 4, 5]))
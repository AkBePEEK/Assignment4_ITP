def length(a):
    return list(filter(lambda x: len(x) > 5, a))


print(length(['hello, world']))
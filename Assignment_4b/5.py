def celcius(a):
    return list(map(lambda x: 5/9 * (x - 32), a))


print(celcius([1, 32, 100, 500]))
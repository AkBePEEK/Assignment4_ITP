def prime_numbers(a):
    return list(filter(lambda x: len([i for i in range(1, x + 1) if x % i == 0]) <= 2, a))


print(prime_numbers([1, 2, 3, 4, 5]))
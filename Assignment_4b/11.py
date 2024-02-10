def fibonacci(n, A=[1, 1]):
    for i in range(n-2):
        A.extend(list(map(lambda x: x[-1] + x[-2], [A])))
    return A


print(fibonacci(10))
def palindromes(a):
    return list(map(lambda x: x[:len(x)//2] == x[x - len(x)//2:], a))
def anagrams(a):
    return list(set(filter(lambda x: len(x) == 2, [tuple(filter(lambda x: set(elem) == set(x), a)) for elem in a])))
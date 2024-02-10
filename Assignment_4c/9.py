def good_num(a: int, b: int = 0, prime: None = None, check: bool = True) -> object:
    if prime is None:
        prime = [2, 3, 5, 7]
    if a == 0:
        return b
    else:
        for i in range(10 ** a - 1, 10 ** (a - 1) - 2, -1):
            for j in range(len(str(i))):
                if (j % 2 == 0 and int(str(i)[j]) % 2 == 0) or (j % 2 == 1 and int(str(i)[j]) in prime):
                    check = True
                else:
                    check = False
                    break
            if check:
                b += 1
    return good_num(a - 1, b)


print(good_num(4))
def palindrome(a):
    if len(a) >= 2:
        if a[len(a) // 2 - 1] != a[len(a) // 2] or a[len(a) // 2] != a[len(a) // 2 + 1]:
            return False
        if len(a) % 2 == 0:
            del a[len(a) // 2 - 1], a[len(a) // 2]
        else:
            del a[len(a) // 2], a[len(a) // 2 + 1]
        return palindrome(a)
    return True


print(palindrome([1,2]))

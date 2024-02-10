def power_of_4(n):
    if n > 4:
        n /= 4
        return power_of_4(n)
    elif 1 < n < 4:
        return False
    else:
        return True


a = int(input())
print(power_of_4(a))
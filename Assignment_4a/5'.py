def hIndex(c,cnt=0):
    for i in range(len(c)):
        if c[i] > i:
            cnt += 1
    return cnt


print(hIndex([0, 1, 3, 5, 6]))

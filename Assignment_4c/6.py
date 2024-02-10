def digits(l1,l2,res=[]):
    if bool(l1) or bool(l2):
        if bool(l2) and bool(l1):
            if l1[0] + l2[0] > 10:
                l1[1] += 1
            res.append((l1[0] + l2[0]) % 10)
            del l1[0], l2[0]
        else:
            res.extend(max(l1, l2))
        return digits(l1, l2)
    return res


print(digits([2,4,3], [5,6,4]))




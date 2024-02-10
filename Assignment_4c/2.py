def func(list1, list2, A=[]):
    if bool(list1) or bool(list2):
        if bool(list1) and bool(list2):
            A.extend([max(list2, list1)[0], min(list1)[0]])
            del list1[0], list2[0]
        else:
            A.append(max(list2, list1)[0])
            del max(list2, list1)[0]
        return func(list1, list2)
    return A


a = [1,2,4]
b = [1,3,4]
print(func(a, b))
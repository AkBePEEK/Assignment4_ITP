def strange_algorithm(n, arr=[], rev=False):
    if not bool(arr):
        arr.extend([i for i in range(1, n + 1)])
    arr.sort(reverse=rev)
    for i in range(len(arr)):
        if i <= len(arr) - 1 and len(arr) > 1:
            del arr[i]
    if len(arr) > 1:
        if rev:
            return strange_algorithm(n, arr, rev=False)
        else:
            return strange_algorithm(n, arr, rev=True)
    return arr[0]
    

print(strange_algorithm(9))
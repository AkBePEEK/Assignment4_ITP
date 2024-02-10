def swap_nodes(head, A=[]):
    if bool(head):
        A.extend([head[1], head[0]])
        del head[1], head[0]
        return swap_nodes(head)
    return A


print(swap_nodes([1,2,3,4]))
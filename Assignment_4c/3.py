def no_val(head, val):
    if val in head:
        del head[head.index(val)]
        return no_val(head, val)
    return head


head, val = [1,2,6,3,4,5,6], 6
print(no_val(head, val))
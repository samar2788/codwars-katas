def max_diff(lst):
    if lst != []:
        lst.sort()
        llen = len(lst)
        return (lst[llen - 1] - lst[0])
    else:
        return 0


d = max_diff([])
print(d)
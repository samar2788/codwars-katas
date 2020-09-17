def descending_order(a):
    b = list(str(a))
    for i in range(len(b)):
        b[i] = int(b[i])
    b.sort(reverse=True)
    c = ''
    for i in b:
        c += str(i)
    return int(c)

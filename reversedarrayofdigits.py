def digitize(n):
    b = list(str(n)[::-1])
    for i in range(0, len(b)):
        b[i] = int(b[i])
    return b

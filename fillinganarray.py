def arr(n=0):
    l = []
    if n == 0 or n == None or n == '':
        return []
    else:
        for i in range(n):
            l.append(i)
    return l

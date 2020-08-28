def swap(a, n):
    l = bin(n).replace('0b', '')
    d = {}
    e = ()
    fl = []
    c = 0
    for i in range(len(a)):
        d[i] = a[i]
    s = ''
    for i in a:
        if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            s += i
    while (c < len(s)):
        for i in range(len(l)):
            try:
                e = s[c], l[i]
                fl.append(e)
                c += 1
            except IndexError:
                pass
    ts = ''
    for x, y in fl:
        if y == '1':
            ts += x.swapcase()
        else:
            ts += x
    temp = list(ts)
    for key, val in d.items():
        if val not in 'abcdefghijklmnopqrstuvwxyz' and val not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp.insert(key, val)
    fs = ''
    for i in temp:
        fs += i
    return fs

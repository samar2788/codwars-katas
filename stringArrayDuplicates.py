from itertools import groupby


def dup(a):
    s = ''
    fl = []
    for k in a:
        j = [i[0] for i in groupby(k)]
        for i in j:
            s += i
        fl.append(s)
        s = ''
    return fl

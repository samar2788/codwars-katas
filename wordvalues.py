from string import ascii_lowercase


def name_value(a):
    l = {}
    s = 0
    cl = []
    fl = []

    for i, j in enumerate(ascii_lowercase):
        l[j] = i+1

    for i in a:
        for j in i:
            for key, val in l.items():
                if j == key:
                    s += val
        cl.append(s)
        s = 0

    for i in range(len(cl)):
        b = (i+1)*cl[i]
        fl.append(b)
    return fl

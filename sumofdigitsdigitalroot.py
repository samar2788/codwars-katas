fl = []


def digital_root(a):
    b = [int(d) for d in str(a)]
    c = sum(b)
    fl.append(c)
    if c >= 10:
        digital_root(c)
    return fl[-1]


print(digital_root(493193))

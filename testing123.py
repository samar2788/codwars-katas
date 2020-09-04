def number(a):
    c = 1
    fl = []
    for i in a:
        s = str(c)+': '+i
        fl.append(s)
        c += 1
    return fl

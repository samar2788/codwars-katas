def find_it(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, val in d.items():
        if val % 2 != 0:
            return key

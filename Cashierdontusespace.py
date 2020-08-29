import itertools


def get_order(a):
    cnt = 0
    y = ()
    fl = []
    cl = []
    s = ' '
    d = {1: 'Burger', 2: 'Fries', 3: 'Chicken',
         4: 'Pizza', 5: 'Sandwich', 6: 'Onionrings', 7: 'Milkshake', 8: 'Coke'}
    for key, val in d.items():
        if val.lower() in a:
            cnt = a.count(val.lower())
            y = val, cnt
            fl.append(y)
    for i in fl:
        item, count = i
        s = count*(item,)
        cl.append(s)
    out = list(itertools.chain(*cl))
    fs = ' '.join(out)
    return fs

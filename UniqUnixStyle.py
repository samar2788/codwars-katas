import itertools


def uniq(a):
    if len(a) == 1 or len(a) == 0:
        return a
    else:
        for i in range(len(a)):
            if a[i] == None:
                a[i] = 'None'
        s = ''.join(a)
        if 'None' in s:
            s = s.strip('None')
            c = ''.join(i for i, _ in itertools.groupby(s))
            ind = a.index('None')
            temp = list(c)
            temp.insert(ind, None)
            return temp
        else:
            c = ''.join(i for i, _ in itertools.groupby(s))
            return list(c)

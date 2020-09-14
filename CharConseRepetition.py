from itertools import groupby


def longest_repetition(a):
    if a == '':
        return('', 0)
    else:
        groups = groupby(a)
        res = [(l, sum(1 for _ in group)) for l, group in groups]
        res.sort(key=lambda x: x[1], reverse=True)
        return res[0]

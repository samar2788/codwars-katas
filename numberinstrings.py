import re


def solve(a):
    l = re.findall(r'\d+', a)
    return max(int(x) for x in l)

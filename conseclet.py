def solve(st):
    l = len(st)
    st = ''.join(sorted(st))
    for i in range(1, l):
        if ord(st[i]) - ord(st[i - 1]) != 1:
            return False
    return True

d=solve("abd")
print(d)
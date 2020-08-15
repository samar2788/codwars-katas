def solve(st):
    n = len(st)

    for res in range(n//2,0,-1):
        prefix = st[0: res]
        suffix = s[n-res:n]
        if (prefix == suffix):
            return res

    return 0
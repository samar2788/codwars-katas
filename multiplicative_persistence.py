def persistence(n, c=0):
    c += 1
    if n < 10:
        return 0
    else:
        l = [int(d) for d in str(n)]
        res = 1
        for i in l:
            res = res*i
        if res < 10:
            return c
        else:
            return persistence(res, c)

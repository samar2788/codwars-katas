def per(n,l=None):
    pr = 1
    num = 0
    if n >= 0 and n < 10:
        return []
    else:
        n = list(str(n))
        for i in n:
            pr = int(i)*pr
        l.append(pr)
        if pr >= 10:
            return per(pr,l)
    return(l)

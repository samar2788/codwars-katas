def roots(a,b,c):
    print(a,b,c)
    d= -(b/a)
    e=(b**2)-(4*a*c)
    if e < 0:
        return None
    else:
        return round(d,2)
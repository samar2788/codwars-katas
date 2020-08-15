def modified_sum(a, n):
    ps = 0
    s =0
    if a!=[] and n>=2:
        for i in a:
            s += i
            ps += i**n
        return (ps - s)
    else:
        return 0


d = modified_sum([1, 2, 3], 3)
print(d)

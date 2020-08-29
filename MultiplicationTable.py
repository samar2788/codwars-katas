def multiplication_table(a):
    l = []
    c = 1
    while c <= a:

        for i in range(1, a+1):
            l.append(c*i)
        c += 1
    tl = list(zip(*[iter(l)]*a))
    return([list(ele) for ele in tl])

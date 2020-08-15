def halving_sum(n):
    i =0
    s =0
    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        while (n/2**i > 1):
            s += int(n/(2**i))
            i += 1
        return (s)

d = halving_sum(1)
print(d)
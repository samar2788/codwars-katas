def reverse_seq(n):
    l = []
    for i in range(1, (n+1)):
        l.append(i)
    l.sort(reverse=True)
    return l

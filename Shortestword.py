def find_short(s):
    s = s.split(' ')
    l = []
    for i in s:
        l.append(len(i))
    l.sort()
    return l[0]

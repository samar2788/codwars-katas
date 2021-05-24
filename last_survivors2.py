def last_survivors(string):
    s = []
    ns = ''
    for i in string:
        s.append(i)
    s = sorted(s)
    l = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    for i in range(len(l)):
        if l[i] == 'z':
            d[l[i]] = 'a'
        else:
            d[l[i]] = l[i+1]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i+1)
            s[i] = d[s[i]]
            break
    if len(s) != len(set(s)):
        return last_survivors(s)
    else:
        return (''.join(s))


print(last_survivors('zzzab'))

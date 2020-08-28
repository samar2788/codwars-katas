Kata :- swap case using n

a = 'how are you today?'
n = 12345
l = bin(n).replace('0b', '')
ll = len(l)
s = ''
fs = ''
d = {}
e = []
lk = []
lv = []
cd = {}
fo = ''
fl = []
for i in a:
    if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        s += i
out = [(s[i:i+ll]) for i in range(0, len(s), ll)]
print(out)
for i in out:
    if len(i) == ll:
        for j in range(ll):
            d[i[j]] = l[j]
        for key, val in d.items():
            lk.append(key)
            lv.append(val)
        d = {}
    else:
        for j in range(len(i)):
            d[i[j]] = l[j]
        for key, val in d.items():
            lk.append(key)
            lv.append(val)
        d = {}
for i in range(len(lv)):
    if lv[i] == '1':
        lk[i] = lk[i].swapcase()
for i in lk:
    fs += i
print(fs)
for i in range(len(a)):
    if a[i] not in 'abcdefghijklmnopqrstuvwxyz' and a[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        cd[i] = a[i]
print(cd)
for key, val in cd.items():
    fo += fs[:key] + val + fs[key:]
    fs = fo
    fo = ''
print(fs)

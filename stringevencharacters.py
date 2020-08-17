a = 'aBc_e9g*i-k$m'
fl = []
if len(a) < 2 or len(a) > 100:
    print("invalid string")
else:
    al = len(a)
    for i in range(al):
        if i % 2 != 0:
            fl.append(a[i])
    print(fl)

a=[12, 13, 14, 15, 16, 17, 18, 20, 21]
al = len(a)
c=a[0]
res={}
l=[]
for i in range(al):
    diff = a[i] - c
    if diff > 1:
        res["i"]=i
        res["n"]=a[i]
        l.append(res)
        res={}
    c = a[i]
print(l)
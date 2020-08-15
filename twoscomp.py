a = [0, 0, 0, 0]
stra = ''
l=[]
for i in a:
    stra+=str(i)
print(stra)
strb =''
for i in stra:
    if i == '0':
        strb+=str('1')
    elif i == '1':
        strb+=str('0')
sm = int(strb,2) + int('1',2)
c = bin(sm)
b = c[2:]
for i in b:
    k = int(i)
    l.append(k)
if len(l) > len(a):
    p = len(l)
    l.pop(l[p-1])
    print(l)
else:
    print(l)

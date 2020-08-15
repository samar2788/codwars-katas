a = [111, 112, 113, 114, 115, 113, 114, 110]
b=[]
b.append(a[0])
b.append(a[1])
b.append(a[-2])
b.append(a[-1])
s1=''
for i in b:
    s1+=chr(i)

a.sort()
d=[]
d.append(a[0])
d.append(a[1])
d.append(a[-2])
d.append(a[-1])
s2=''
for i in d:
    s2+=chr(i)


a.sort(reverse=True)
e=[]
e.append(a[0])
e.append(a[1])
e.append(a[-2])
e.append(a[-1])
s3=''
for i in e:
    s3+=chr(i)

print(s1+'-'+s2+'-'+s3+'-'+s2)


# def extract(arr): return ''.join(arr[:2]+arr[-2:])

# def sort_transform(arr):
#     arr = list(map(chr,arr))
#     w1  = extract(arr)
#     arr.sort()
#     w2  = extract(arr)
#     return f'{w1}-{w2}-{w2[::-1]}-{w2}'
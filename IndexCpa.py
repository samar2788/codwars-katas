s = "codewarriors"
ind = [5]
sl = len(s)
ls = []
st=''
for i in s:
    ls.append(i)
print(ls)

for i in range(sl):
    if i in ind:
        ls[i]=ls[i].upper()
print(ls)
for i in ls:
    st +=i
print(st)